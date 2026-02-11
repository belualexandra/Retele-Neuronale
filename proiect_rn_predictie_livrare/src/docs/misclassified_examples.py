import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

MODEL_PATH = "models/best_model.keras"
PIPELINE_PATH = "config/preprocessing_pipeline.joblib"
TEST_PATH = "data/test/test.csv"   

LABELS = ["Fast", "Medium", "Slow"]

def main():
    # Load model & pipeline
    model = load_model(MODEL_PATH)
    pipeline = joblib.load(PIPELINE_PATH)

    # Load test data
    df = pd.read_csv(TEST_PATH)

    X = df.drop(columns=["Delivery_Time_min", "Delivery_Class"])
    y_true = df["Delivery_Class"].values

    X_proc = pipeline.transform(X)

    # Predict
    _, probs = model.predict(X_proc, verbose=0)
    y_pred = np.argmax(probs, axis=1)
    confidences = np.max(probs, axis=1)

    # Find misclassified
    wrong_idx = np.where(y_true != y_pred)[0]

    print("Primele 5 exemple greșite:\n")
    for i in wrong_idx[:5]:
        print(f"Index: {i}")
        print(f" True label: {LABELS[y_true[i]]}")
        print(f" Predicted:  {LABELS[y_pred[i]]}")
        print(f" Confidence: {confidences[i]:.2f}")
        print("-" * 40)

if __name__ == "__main__":
    main()
