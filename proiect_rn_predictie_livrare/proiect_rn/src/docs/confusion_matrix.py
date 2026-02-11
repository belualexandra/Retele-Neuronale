import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from joblib import load as joblib_load

MODEL_PATH = "models/train_model.keras"
PIPELINE_PATH = "config/preprocessing_pipeline.joblib"
TEST_PATH = "data/test/test.csv"

OUT_DIR = "docs"
OUT_PATH = os.path.join(OUT_DIR, "confusion_matrix.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    # 1) Load model + pipeline
    model = load_model(MODEL_PATH)
    print("✓ Model încărcat")

    pipeline = joblib_load(PIPELINE_PATH)
    print("✓ Pipeline încărcat")

    # 2) Load test.csv
    if not os.path.exists(TEST_PATH):
        raise FileNotFoundError(f"Lipsește {TEST_PATH}")

    test_df = pd.read_csv(TEST_PATH)

    # 3) y_true (clase reale)
    if "Delivery_Class" not in test_df.columns:
        raise ValueError("În test.csv nu există coloana Delivery_Class")

    y_test_cls = test_df["Delivery_Class"].values

    # 4) X_raw = toate coloanele, mai puțin țintele
    drop_cols = ["Delivery_Class"]
    # dacă există și minutele în test.csv, le scoatem din input (țintă regresie)
    if "Delivery_Time_min" in test_df.columns:
        drop_cols.append("Delivery_Time_min")

    X_test_raw = test_df.drop(columns=drop_cols)

    # 5) Transform cu pipeline-ul din training
    X_test = pipeline.transform(X_test_raw)

    # 6) Predict (multitask): [minutes_pred, class_probs]
    y_pred_minutes, y_pred_probs = model.predict(X_test, verbose=0)
    y_pred_cls = np.argmax(y_pred_probs, axis=1)

    # 7) Confusion matrix + save
    cm = confusion_matrix(y_test_cls, y_pred_cls)

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Fast", "Medium", "Slow"]
    )
    disp.plot(cmap="Blues", values_format="d")

    plt.title("Confusion Matrix – Delivery Class (Test Set)")
    plt.tight_layout()
    plt.savefig(OUT_PATH, dpi=200)
    plt.close()

    print(f"✓ Matricea de confuzie salvată în: {OUT_PATH}")


if __name__ == "__main__":
    main()
