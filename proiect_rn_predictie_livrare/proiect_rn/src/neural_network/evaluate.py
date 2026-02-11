import os
import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse

from tensorflow.keras.models import load_model
from sklearn.metrics import (
    accuracy_score, 
    f1_score, 
    mean_absolute_error, 
    mean_squared_error,
    confusion_matrix,
    ConfusionMatrixDisplay
)


MODEL_PATH = "models/best_model.keras"
PIPELINE_PATH = "config/preprocessing_params.pkl"
TEST_CSV = "data/test/test.csv"
RESULTS_DIR = "results"
DOCS_DIR = "docs"

def evaluate_model(model_path, data_path, pipeline_path):
    print(f" Încărcare model din: {model_path}")
    model = load_model(model_path)
    
    print(f" Încărcare pipeline din: {pipeline_path}")
    pipeline = joblib.load(pipeline_path)
    
    print(f" Încărcare date de test din: {data_path}")
    df_test = pd.read_csv(data_path)
    
    
    if "Delivery_Time_min" not in df_test.columns or "Delivery_Class" not in df_test.columns:
        raise ValueError("Datasetul de test trebuie să conțină coloanele țintă.")
        
    X_test_raw = df_test.drop(columns=["Delivery_Time_min", "Delivery_Class"])
    y_test_minutes = df_test["Delivery_Time_min"].values
    y_test_class = df_test["Delivery_Class"].values
    
    
    X_test = pipeline.transform(X_test_raw)
    
    
    print(" Rulare inferență...")
    pred_minutes, pred_class_probs = model.predict(X_test, verbose=0)
    
   
    pred_minutes = pred_minutes.flatten()
    pred_class = np.argmax(pred_class_probs, axis=1)
    
    
    metrics = {
        "mae_minutes": float(mean_absolute_error(y_test_minutes, pred_minutes)),
        "rmse_minutes": float(np.sqrt(mean_squared_error(y_test_minutes, pred_minutes))),
        "accuracy_class": float(accuracy_score(y_test_class, pred_class)),
        "f1_macro_class": float(f1_score(y_test_class, pred_class, average="macro"))
    }
    
    print("\n REZULTATE EVALUARE:")
    print(f"    MAE (Minute): {metrics['mae_minutes']:.4f}")
    print(f"    Accuracy:     {metrics['accuracy_class']:.4f}")
    print(f"    F1-Score:     {metrics['f1_macro_class']:.4f}")
    
    
    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_file = os.path.join(RESULTS_DIR, "evaluation_metrics.json")
    with open(out_file, "w") as f:
        json.dump(metrics, f, indent=4)
    print(f" Metrici salvate în: {out_file}")

    
    cm = confusion_matrix(y_test_class, pred_class)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fast", "Medium", "Slow"])
    
    os.makedirs(DOCS_DIR, exist_ok=True)
    cm_path = os.path.join(DOCS_DIR, "confusion_matrix_eval.png")
    
    fig, ax = plt.subplots(figsize=(6, 5))
    disp.plot(cmap="Blues", ax=ax)
    plt.title("Confusion Matrix (Test Set)")
    plt.savefig(cm_path)
    plt.close()
    print(f" Matrice de confuzie salvată în: {cm_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default=MODEL_PATH, help="Calea către modelul antrenat")
    args = parser.parse_args()
    
    evaluate_model(args.model, TEST_CSV, PIPELINE_PATH)