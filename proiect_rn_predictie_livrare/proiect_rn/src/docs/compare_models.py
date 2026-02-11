import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

PIPELINE_PATH = "config/preprocessing_pipeline.joblib"
TEST_PATH = "data/test/test.csv"

BEST = "models/best_model.keras"
TRAINED = "models/trained_model.keras"

def main():
    df = pd.read_csv(TEST_PATH)

    X = df.drop(columns=["Delivery_Time_min", "Delivery_Class"])
    y_true = df["Delivery_Class"].values

    pipe = joblib.load(PIPELINE_PATH)
    Xp = pipe.transform(X)

    m_best = load_model(BEST)
    m_tr = load_model(TRAINED)

    # multitask outputs: [minutes, class_probs]
    _, p_best = m_best.predict(Xp, verbose=0)
    _, p_tr = m_tr.predict(Xp, verbose=0)

    y_best = np.argmax(p_best, axis=1)
    y_tr = np.argmax(p_tr, axis=1)

    same_labels = np.mean(y_best == y_tr)
    max_prob_diff = np.max(np.abs(p_best - p_tr))
    mean_prob_diff = np.mean(np.abs(p_best - p_tr))

    print(f"Same predicted labels ratio: {same_labels:.6f}")
    print(f"Mean abs prob diff:        {mean_prob_diff:.8f}")
    print(f"Max abs prob diff:         {max_prob_diff:.8f}")

    # Also compare accuracy vs ground truth
    acc_best = np.mean(y_best == y_true)
    acc_tr = np.mean(y_tr == y_true)
    print(f"Accuracy best:   {acc_best:.6f}")
    print(f"Accuracy trained:{acc_tr:.6f}")

if __name__ == "__main__":
    main()
