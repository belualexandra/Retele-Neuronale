import os
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

PIPE_PKL = "config/preprocessing_params.pkl"
PIPE_JOBLIB = "config/preprocessing_pipeline.joblib"

NUM_COLS = ["Distance_km", "Preparation_Time_min", "Courier_Experience_yrs", "Is_RushHour"]
CAT_COLS = ["Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type"]

def main():
    train = pd.read_csv("data/train/train.csv")

    pre = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUM_COLS),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CAT_COLS),
        ]
    )

    pipe = Pipeline([("pre", pre)])
    pipe.fit(train[NUM_COLS + CAT_COLS])

    os.makedirs("config", exist_ok=True)
    joblib.dump(pipe, PIPE_PKL)      # cerut în README
    joblib.dump(pipe, PIPE_JOBLIB)   # util pentru tine

    # mic raport
    X = pipe.transform(train[NUM_COLS + CAT_COLS])
    print("✓ Saved preprocessing pipeline:")
    print(f" - {PIPE_PKL}")
    print(f" - {PIPE_JOBLIB}")
    print(f"Train transformed shape: {X.shape}")

if __name__ == "__main__":
    main()
