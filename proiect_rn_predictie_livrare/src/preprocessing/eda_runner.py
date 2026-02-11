import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Config
# -----------------------------
DATA_PATH = "data/processed/featured.csv"

OUT_BASE = "reports/eda"
OUT_31 = os.path.join(OUT_BASE, "3_1_statistici")
OUT_32 = os.path.join(OUT_BASE, "3_2_calitate")
OUT_33 = os.path.join(OUT_BASE, "3_3_probleme")

TARGET_REG = "Delivery_Time_min"
TARGET_CLASS = "Delivery_Class"

NUM_COLS = ["Distance_km", "Preparation_Time_min", "Courier_Experience_yrs", TARGET_REG]
CAT_COLS = ["Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type", TARGET_CLASS]

RANDOM_STATE = 42


# -----------------------------
# Helpers
# -----------------------------
def ensure_dirs():
    for p in [OUT_31, OUT_32, OUT_33]:
        os.makedirs(p, exist_ok=True)


def save_df(df: pd.DataFrame, path: str):
    df.to_csv(path, index=True)


def plot_histograms(df: pd.DataFrame, cols, out_dir: str, bins: int = 30):
    for col in cols:
        plt.figure()
        series = df[col].dropna()
        plt.hist(series, bins=bins)
        plt.title(f"Histogram - {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        out_path = os.path.join(out_dir, f"hist_{col}.png")
        plt.tight_layout()
        plt.savefig(out_path, dpi=160)
        plt.close()


def plot_boxplots(df: pd.DataFrame, cols, out_dir: str):
    for col in cols:
        plt.figure()
        series = df[col].dropna()
        plt.boxplot(series, vert=True)
        plt.title(f"Boxplot - {col}")
        plt.ylabel(col)
        out_path = os.path.join(out_dir, f"box_{col}.png")
        plt.tight_layout()
        plt.savefig(out_path, dpi=160)
        plt.close()


def iqr_outliers(series: pd.Series):
    """Return outlier indices using IQR rule."""
    s = series.dropna()
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    low = q1 - 1.5 * iqr
    high = q3 + 1.5 * iqr
    mask = (series < low) | (series > high)
    return mask, low, high


# -----------------------------
# EDA 3.1 - Statistici descriptive
# -----------------------------
def eda_3_1(df: pd.DataFrame):
    # a) describe + quartile
    desc = df[NUM_COLS].describe().T  # count, mean, std, min, 25,50,75,max
    save_df(desc, os.path.join(OUT_31, "descriptive_stats_numeric.csv"))

    # b) median separate (ca să fie explicit cerința)
    med = df[NUM_COLS].median(numeric_only=True).to_frame(name="median")
    save_df(med, os.path.join(OUT_31, "median_numeric.csv"))

    # c) min-max separate
    minmax = pd.DataFrame({
        "min": df[NUM_COLS].min(numeric_only=True),
        "max": df[NUM_COLS].max(numeric_only=True),
    })
    save_df(minmax, os.path.join(OUT_31, "minmax_numeric.csv"))

    # d) distribuții (histograme)
    plot_histograms(df, NUM_COLS, OUT_31, bins=30)

    # e) outlieri (boxplot + tabel outliers IQR + percentile)
    plot_boxplots(df, NUM_COLS, OUT_31)

    out_summary = []
    for col in NUM_COLS:
        mask, low, high = iqr_outliers(df[col])
        out_count = int(mask.sum())
        p01 = float(df[col].quantile(0.01))
        p99 = float(df[col].quantile(0.99))
        out_summary.append({
            "feature": col,
            "iqr_low": float(low),
            "iqr_high": float(high),
            "iqr_outliers_count": out_count,
            "p01": p01,
            "p99": p99
        })

    out_df = pd.DataFrame(out_summary).set_index("feature")
    save_df(out_df, os.path.join(OUT_31, "outliers_iqr_and_percentiles.csv"))


# -----------------------------
# EDA 3.2 - Calitatea datelor
# -----------------------------
def eda_3_2(df: pd.DataFrame):
    # a) missing values %
    miss = pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_percent": (df.isna().mean() * 100).round(3)
    }).sort_values("missing_percent", ascending=False)
    save_df(miss, os.path.join(OUT_32, "missing_values_report.csv"))

    # b) valori inconsistente/eronate (reguli simple, demonstrabile)
    checks = []

    # Reguli de domeniu (se pot extinde dacă profesorul cere):
    # - Distance_km, Preparation_Time_min, Courier_Experience_yrs, Delivery_Time_min nu trebuie negative
    for col in ["Distance_km", "Preparation_Time_min", "Courier_Experience_yrs", TARGET_REG]:
        neg_count = int((df[col] < 0).sum()) if col in df.columns else 0
        checks.append({"check": f"{col}_negative_values", "count": neg_count})

    # - Order_ID unic?
    if "Order_ID" in df.columns:
        dup_ids = int(df["Order_ID"].duplicated().sum())
    else:
        dup_ids = 0
    checks.append({"check": "duplicated_Order_ID", "count": dup_ids})

    # - duplicate rows
    dup_rows = int(df.duplicated().sum())
    checks.append({"check": "duplicated_rows", "count": dup_rows})

    # - categorii “neobișnuite” (top categories)
    cat_summary = {}
    for col in ["Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type"]:
        if col in df.columns:
            cat_summary[col] = df[col].astype(str).value_counts().head(20).to_dict()

    with open(os.path.join(OUT_32, "quality_checks.json"), "w", encoding="utf-8") as f:
        json.dump({"checks": checks, "top_categories": cat_summary}, f, indent=2, ensure_ascii=False)

    # c) corelații (numeric) + export matrice
    corr = df[NUM_COLS].corr(numeric_only=True)
    save_df(corr, os.path.join(OUT_32, "correlation_matrix_numeric.csv"))

    # heatmap simplu (fără seaborn)
    plt.figure()
    plt.imshow(corr.values, aspect="auto")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
    plt.yticks(range(len(corr.index)), corr.index)
    plt.colorbar()
    plt.title("Correlation heatmap (numeric)")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_32, "correlation_heatmap_numeric.png"), dpi=160)
    plt.close()


# -----------------------------
# EDA 3.3 - Probleme identificate (automat, pe baza rapoartelor)
# -----------------------------
def eda_3_3(df: pd.DataFrame):
    problems = []

    # 1) Missing > 0%
    miss_pct = df.isna().mean() * 100
    for col, pct in miss_pct.sort_values(ascending=False).items():
        if pct > 0:
            problems.append(f"Coloana '{col}' are {pct:.2f}% valori lipsă.")

    # 2) Distribuții neuniforme la categorice (dominant category > 80%)
    for col in ["Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type"]:
        if col in df.columns:
            vc = df[col].astype(str).value_counts(normalize=True)
            if len(vc) > 0 and float(vc.iloc[0]) > 0.80:
                problems.append(
                    f"Caracteristica categorială '{col}' este neuniformă: "
                    f"categoria dominantă are {float(vc.iloc[0])*100:.1f}%."
                )

    # 3) Class imbalance (pentru Delivery_Class): dacă o clasă > 70%
    if TARGET_CLASS in df.columns:
        vc = df[TARGET_CLASS].value_counts(normalize=True).sort_index()
        max_share = float(vc.max())
        if max_share > 0.70:
            problems.append(
                f"Dezechilibru de clase în '{TARGET_CLASS}': clasa dominantă are {max_share*100:.1f}%."
            )
        else:
            problems.append(
                f"Distribuția claselor în '{TARGET_CLASS}' este relativ echilibrată "
                f"(max {max_share*100:.1f}%)."
            )

    # 4) Corelații foarte puternice > 0.9 (potențial redundanță)
    corr = df[NUM_COLS].corr(numeric_only=True).abs()
    strong_pairs = []
    cols = corr.columns.tolist()
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            val = float(corr.iloc[i, j])
            if val > 0.90:
                strong_pairs.append((cols[i], cols[j], val))
    if strong_pairs:
        for a, b, v in strong_pairs:
            problems.append(f"Corelație foarte puternică între '{a}' și '{b}': |r|={v:.3f} (posibil redundant).")
    else:
        problems.append("Nu s-au identificat corelații extrem de ridicate (|r|>0.90) între variabilele numerice.")

    # 5) Outliers IQR (raport sumar)
    for col in NUM_COLS:
        mask, low, high = iqr_outliers(df[col])
        out_count = int(mask.sum())
        out_share = (out_count / len(df)) * 100
        if out_share > 1.0:
            problems.append(
                f"'{col}' are {out_count} outlieri IQR (~{out_share:.2f}%). Interval IQR: [{low:.2f}, {high:.2f}]."
            )

    # Save as TXT (ușor de pus în raport)
    out_txt = os.path.join(OUT_33, "problems_identified.txt")
    with open(out_txt, "w", encoding="utf-8") as f:
        for p in problems:
            f.write("- " + p + "\n")

    # Save also as JSON (dacă vrei structură)
    with open(os.path.join(OUT_33, "problems_identified.json"), "w", encoding="utf-8") as f:
        json.dump({"problems": problems}, f, indent=2, ensure_ascii=False)


def main():
    ensure_dirs()

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            f"Nu găsesc {DATA_PATH}. Rulează mai întâi Etapa 3: "
            "data_cleaner.py + feature_engineering.py."
        )

    df = pd.read_csv(DATA_PATH)

    # EDA pe cerințe
    eda_3_1(df)
    eda_3_2(df)
    eda_3_3(df)

    print("✓ EDA complet. Rezultatele au fost salvate în:")
    print(f"  - {OUT_31}")
    print(f"  - {OUT_32}")
    print(f"  - {OUT_33}")


if __name__ == "__main__":
    main()
