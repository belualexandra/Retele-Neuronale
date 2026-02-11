import os
import pandas as pd

PUBLIC_PATH = "data/raw/Food_Delivery_Times.csv"
GENERATED_PATH = "data/generated/generated_data.csv"
OUT_PATH = "data/raw/combined_raw.csv"

def main():
    if not os.path.exists(PUBLIC_PATH):
        raise FileNotFoundError(f"Lipsește {PUBLIC_PATH}")

    if not os.path.exists(GENERATED_PATH):
        raise FileNotFoundError(
            f"Lipsește {GENERATED_PATH}. Rulează întâi generatorul din Etapa 4 "
            "(src/data_acquisition/generate.py)."
        )

    public_df = pd.read_csv(PUBLIC_PATH)
    gen_df = pd.read_csv(GENERATED_PATH)

    # Verificare coloane compatibile (ca să nu combini greșit)
    if set(public_df.columns) != set(gen_df.columns):
        raise ValueError(
            "Coloanele nu coincid între datasetul public și cel generat.\n"
            f"Public: {list(public_df.columns)}\n"
            f"Generated: {list(gen_df.columns)}"
        )

    # Reindex Order_ID pentru a evita coliziuni
    max_id = public_df["Order_ID"].max()
    gen_df = gen_df.copy()
    gen_df["Order_ID"] = gen_df["Order_ID"] + max_id

    combined = pd.concat([public_df, gen_df], ignore_index=True)

    os.makedirs("data/raw", exist_ok=True)
    combined.to_csv(OUT_PATH, index=False)

    ratio = len(gen_df) / len(combined)
    print(f"✓ Combined dataset saved to: {OUT_PATH}")
    print(f"Total rows: {len(combined)}")
    print(f"Generated rows: {len(gen_df)} ({ratio*100:.1f}%)")

if __name__ == "__main__":
    main()
