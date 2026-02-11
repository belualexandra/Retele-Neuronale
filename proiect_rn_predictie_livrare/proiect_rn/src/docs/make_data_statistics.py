import os
import pandas as pd

REAL_PATH = "data/raw/Food_Delivery_Times.csv"
GEN_PATH = "data/generated/generated_data.csv"
OUT_PATH = "docs/data_statistics.csv"

NUM_COLS = ["Delivery_Time_min", "Distance_km", "Preparation_Time_min", "Courier_Experience_yrs"]
CAT_COLS = ["Traffic_Level", "Weather", "Time_of_Day", "Vehicle_Type"]

def stats_numeric(df: pd.DataFrame, label: str) -> pd.DataFrame:
    desc = df[NUM_COLS].describe().T
    desc["dataset"] = label
    # missing %
    desc["missing_percent"] = (df[NUM_COLS].isna().mean() * 100).values
    return desc.reset_index(names="feature")

def stats_categorical(df: pd.DataFrame, label: str) -> pd.DataFrame:
    rows = []
    for col in CAT_COLS:
        vc = df[col].value_counts(dropna=False, normalize=True) * 100
        for k, v in vc.items():
            rows.append({
                "dataset": label,
                "feature": col,
                "category": str(k),
                "percent": float(v)
            })
    return pd.DataFrame(rows)

def main():
    if not os.path.exists(REAL_PATH):
        raise FileNotFoundError(f"Lipsește {REAL_PATH}")
    if not os.path.exists(GEN_PATH):
        raise FileNotFoundError(f"Lipsește {GEN_PATH}")

    os.makedirs("docs", exist_ok=True)

    real = pd.read_csv(REAL_PATH)
    gen = pd.read_csv(GEN_PATH)

    num_real = stats_numeric(real, "real")
    num_gen = stats_numeric(gen, "generated")

    cat_real = stats_categorical(real, "real")
    cat_gen = stats_categorical(gen, "generated")

    # salvăm în același CSV, în 2 secțiuni (numeric + categorical)
    # ca să fie ușor de pus în raport.
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("### NUMERIC_STATS\n")
    num_all = pd.concat([num_real, num_gen], ignore_index=True)
    num_all.to_csv(OUT_PATH, mode="a", index=False)

    with open(OUT_PATH, "a", encoding="utf-8") as f:
        f.write("\n### CATEGORICAL_DISTRIBUTIONS\n")
    cat_all = pd.concat([cat_real, cat_gen], ignore_index=True)
    cat_all.to_csv(OUT_PATH, mode="a", index=False)

    print(f"✓ Saved: {OUT_PATH}")

if __name__ == "__main__":
    main()
