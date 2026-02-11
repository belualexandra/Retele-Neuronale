import os
import pandas as pd

IN_PATH = "data/processed/cleaned.csv"
OUT_PATH = "data/processed/featured.csv"

TARGET = "Delivery_Time_min"

def make_delivery_class(y: pd.Series) -> pd.Series:
    # Binning în 3 clase (poți ajusta mai târziu după distribuție)
    # 0 = fast, 1 = medium, 2 = slow
    return pd.cut(
        y,
        bins=[-float("inf"), 40, 70, float("inf")],
        labels=[0, 1, 2]
    ).astype(int)

def main():
    os.makedirs("data/processed", exist_ok=True)
    df = pd.read_csv(IN_PATH)

    # feature simplu: total_time = preparation + delivery (doar ca exemplu)
    # Atenție: NU folosim Delivery_Time_min ca feature la training! (ar fi leakage)
    df["Is_RushHour"] = df["Time_of_Day"].isin(["Morning", "Evening"]).astype(int)

    # label pentru clasificare (folosit în Etapa 5)
    df["Delivery_Class"] = make_delivery_class(df[TARGET])

    df.to_csv(OUT_PATH, index=False)
    print(f"✓ Saved featured data to: {OUT_PATH}")
    print("Class distribution:")
    print(df["Delivery_Class"].value_counts(normalize=True).sort_index())

if __name__ == "__main__":
    main()
