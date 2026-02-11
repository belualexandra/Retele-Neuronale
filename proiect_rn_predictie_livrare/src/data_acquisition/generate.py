import os
import json
import numpy as np
import pandas as pd

# INPUT (dataset public)
REAL_PATH = "data/raw/Food_Delivery_Times.csv"

# OUTPUT (date generate + raport)
OUT_CSV = "data/generated/generated_data.csv"
OUT_JSON = "data/generated/generation_report.json"

N_SAMPLES = 10000
RANDOM_STATE = 42

# Intervalele (bins) pentru generarea uniformă a valorilor numerice.
# Acest lucru previne situația în care avem prea puține date pentru distanțe mari sau experiență multă.
DIST_BINS = [0.0, 4.0, 8.0, 12.0, 16.0, 20.0]     # km
EXP_BINS = [-0.5, 1, 3, 6, 10, 30]                 # ani

# Coloanele EXACT ca în datasetul public (compatibil cu combine_datasets.py)
PUBLIC_COLUMNS = [
    "Order_ID",
    "Distance_km",
    "Weather",
    "Traffic_Level",
    "Time_of_Day",
    "Vehicle_Type",
    "Preparation_Time_min",
    "Courier_Experience_yrs",
    "Delivery_Time_min",
]

CAT_COLS = ["Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type"]


def _sample_uniform_bins(rng, bins, n, sampler):
    """
    Funcție critică pentru echilibrarea datelor.
    Împarte numărul total de mostre (n) în mod egal pe fiecare interval din 'bins'.
    Astfel, ne asigurăm că avem date și pentru distanțe mici, și pentru mari.
    """
    k = len(bins) - 1
    base = n // k
    rem = n % k
    sizes = [base + (1 if i < rem else 0) for i in range(k)]

    out = []
    for i in range(k):
        low, high = bins[i], bins[i + 1]
        out.append(sampler(low, high, sizes[i]))
    return np.concatenate(out)


def _pmf_sample(rng, series: pd.Series, n: int):
    """
    Probability Mass Function (PMF) Sampling.
    În loc să generăm uniform (ex: 25% ploaie, 25% soare),
    ne uităm la datele reale: dacă în realitate plouă doar 10% din timp,
    vom genera 'Rainy' doar în 10% din cazuri.
    """
    vc = series.value_counts(normalize=True)
    cats = vc.index.to_list()
    probs = vc.values
    return rng.choice(cats, size=n, p=probs)


def _jsonify(obj):
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    return obj


def main():
    # Inițializăm generatorul de numere aleatoare
    rng = np.random.default_rng(RANDOM_STATE)

    if not os.path.exists(REAL_PATH):
        raise FileNotFoundError(f"Lipsește {REAL_PATH}")
    
    # Încărcăm datele reale pentru analiză
    real = pd.read_csv(REAL_PATH)

    # verificăm că public are coloanele așteptate
    missing = [c for c in PUBLIC_COLUMNS if c not in real.columns]
    if missing:
        raise ValueError(f"Datasetul public nu are coloanele: {missing}")

    # --- categorice: păstrăm distribuțiile reale 
    weather = _pmf_sample(rng, real["Weather"], N_SAMPLES)
    traffic = _pmf_sample(rng, real["Traffic_Level"], N_SAMPLES)
    tod = _pmf_sample(rng, real["Time_of_Day"], N_SAMPLES)
    veh = _pmf_sample(rng, real["Vehicle_Type"], N_SAMPLES)

    # --- numerice: acoperire mai uniformă

    distance = _sample_uniform_bins(
        rng, DIST_BINS, N_SAMPLES,
        lambda low, high, size: rng.uniform(max(0.1, low), high, size=size)
    )
    distance = np.round(distance, 2)

    # Experience: uniform intre 0 si 30 de ani
    exp = _sample_uniform_bins(
        rng, EXP_BINS, N_SAMPLES,
        lambda low, high, size: rng.integers(
            max(0, int(np.ceil(low))), int(np.floor(high)) + 1, size=size
        )
    )
    exp = np.clip(exp, 0, 30).astype(int)

    # Preparation: distribuție realistă (majoritatea în jur de 15 min, min 5, max 35)
    prep = rng.triangular(left=5, mode=15, right=35, size=N_SAMPLES)
    prep = np.round(prep).astype(int)
    prep = np.clip(prep, 1, 120)


    # Identificăm orele de vârf (Rush Hour) pentru penalizare
    is_rush = np.isin(tod, ["Morning", "Evening"]).astype(int)

    # Timpul de bază: Timp preparare + 2.2 min per km (viteză medie estimată)
    base = prep + distance * 2.2

    traffic_pen = np.where(traffic == "Low", 0, np.where(traffic == "Medium", 6, 12))

    weather_pen = np.select(
        [
            weather == "Clear",
            weather == "Windy",
            weather == "Foggy",
            weather == "Rainy",
            weather == "Snowy",
        ],
        [0, 3, 5, 7, 10],
        default=4
    )

    veh_pen = np.where(veh == "Bike", 6, np.where(veh == "Scooter", 2, 0))
    rush_pen = is_rush * 4

    # Bonus experiență (curierii vechi sunt mai rapizi, scădem timp)
    exp_bonus = np.clip(exp, 0, 10) * 0.6

    noise = rng.normal(0, 3.0, size=N_SAMPLES)

    delivery_time = base + traffic_pen + weather_pen + veh_pen + rush_pen - exp_bonus + noise
    delivery_time = np.clip(delivery_time, 10, 180)
    delivery_time = np.round(delivery_time, 1)

    # Order_ID unic
    start_id = int(pd.to_numeric(real["Order_ID"], errors="coerce").max()) + 1
    order_id = np.arange(start_id, start_id + N_SAMPLES)

    gen = pd.DataFrame({
        "Order_ID": order_id,
        "Distance_km": distance,
        "Weather": weather,
        "Traffic_Level": traffic,
        "Time_of_Day": tod,
        "Vehicle_Type": veh,
        "Preparation_Time_min": prep,
        "Courier_Experience_yrs": exp,
        "Delivery_Time_min": delivery_time,
    })[PUBLIC_COLUMNS]

    os.makedirs("data/generated", exist_ok=True)
    gen.to_csv(OUT_CSV, index=False)

    # --- raport JSON 
    report = {
        "real_path": REAL_PATH,
        "out_csv": OUT_CSV,
        "out_json": OUT_JSON,
        "n_samples_generated": int(N_SAMPLES),
        "random_state": int(RANDOM_STATE),
        "columns_generated": PUBLIC_COLUMNS,
        "distance_bins": DIST_BINS,
        "experience_bins": EXP_BINS,
        "distance_bin_percent_generated": {
            str(k): _jsonify(v) for k, v in (
                pd.cut(gen["Distance_km"], DIST_BINS).value_counts(normalize=True).sort_index() * 100
            ).to_dict().items()
        },
        "experience_bin_percent_generated": {
            str(k): _jsonify(v) for k, v in (
                pd.cut(gen["Courier_Experience_yrs"], EXP_BINS).value_counts(normalize=True).sort_index() * 100
            ).to_dict().items()
        },
        "categorical_percent_generated": {},
        "numeric_summary_generated": {},
        "notes": [
            "Generator produces ONLY the public-compatible columns (no Is_RushHour in raw).",
            "Distance_km and Courier_Experience_yrs are generated with bin-uniform coverage to avoid missing tails.",
            "Categorical columns are sampled from the real dataset PMF to remain realistic."
        ]
    }

    for col in CAT_COLS:
        vc = (pd.Series(gen[col]).value_counts(normalize=True) * 100).to_dict()
        report["categorical_percent_generated"][col] = {str(k): _jsonify(v) for k, v in vc.items()}

    for col in ["Distance_km", "Preparation_Time_min", "Courier_Experience_yrs", "Delivery_Time_min"]:
        desc = gen[col].describe().to_dict()
        report["numeric_summary_generated"][col] = {k: _jsonify(v) for k, v in desc.items()}

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"✓ Generated saved to: {OUT_CSV}")
    print(f"✓ Report saved to:   {OUT_JSON}")
    print(f"Rows: {len(gen)}")


if __name__ == "__main__":
    main()
