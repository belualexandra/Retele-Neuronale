import os
import pandas as pd
from sklearn.model_selection import train_test_split

IN_PATH = "data/processed/featured.csv"

RANDOM_STATE = 42
TEST_SIZE = 0.15
VAL_SIZE = 0.15  # din total

LABEL_CLASS = "Delivery_Class"  # pentru stratificare la clasificare

def main():
    df = pd.read_csv(IN_PATH)

    # 1) test split (15%)
    trainval, test = train_test_split(
        df,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=df[LABEL_CLASS]
    )

    # 2) validation split (15% din total => val_frac din trainval)
    val_frac = VAL_SIZE / (1.0 - TEST_SIZE)  # ~0.17647
    train, val = train_test_split(
        trainval,
        test_size=val_frac,
        random_state=RANDOM_STATE,
        stratify=trainval[LABEL_CLASS]
    )

    # 3) save
    os.makedirs("data/train", exist_ok=True)
    os.makedirs("data/validation", exist_ok=True)
    os.makedirs("data/test", exist_ok=True)

    train.to_csv("data/train/train.csv", index=False)
    val.to_csv("data/validation/validation.csv", index=False)
    test.to_csv("data/test/test.csv", index=False)

    print("✓ Split done.")
    print(f"Train: {len(train)} | Val: {len(val)} | Test: {len(test)}")

if __name__ == "__main__":
    main()
