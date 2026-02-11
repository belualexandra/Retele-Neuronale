import os
import pandas as pd

RAW_PATH = "data/raw/combined_raw.csv"
OUT_PATH = "data/processed/cleaned.csv"

CATEGORICAL = ["Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type"]
NUMERICAL = ["Distance_km", "Preparation_Time_min", "Courier_Experience_yrs"]
TARGET = "Delivery_Time_min"

def main():
    os.makedirs("data/processed", exist_ok=True)

    df = pd.read_csv(RAW_PATH)

    # 1) basic checks
    expected = set(CATEGORICAL + NUMERICAL + ["Order_ID", TARGET])
    missing_cols = expected - set(df.columns)
    if missing_cols:
        raise ValueError(f"Lipsesc coloane din CSV: {missing_cols}")

    # 2) remove duplicates
    df = df.drop_duplicates()

    # 3) imputare valori lipsă
    for col in CATEGORICAL:
        if df[col].isna().any():
            df[col] = df[col].fillna("Unknown")

    for col in NUMERICAL:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].median())

    # 4) cap outliers doar pe target (opțional, dar stabil)
    # (Etapa 3 cere tratarea outlierilor; aici facem winsorize la 99%)
    p99 = df[TARGET].quantile(0.99)
    df[TARGET] = df[TARGET].clip(upper=p99)

    df.to_csv(OUT_PATH, index=False)
    print(f"✓ Saved cleaned data to: {OUT_PATH}")
    print(f"Rows: {len(df)}")

if __name__ == "__main__":
    main()
