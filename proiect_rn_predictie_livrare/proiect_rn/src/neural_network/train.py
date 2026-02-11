import os
import json
import joblib
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.metrics import (
    f1_score,
    accuracy_score,
    classification_report,
    mean_absolute_error,
    mean_squared_error
)

from src.neural_network.model import build_multitask_model

# -----------------------------
# Config
# -----------------------------
PIPE_PATH = "config/preprocessing_params.pkl"   # cerut
MODEL_DIR = "models"
RESULTS_DIR = "results"

MODEL_OUT = os.path.join(MODEL_DIR, "trained_model.keras")
BEST_MODEL_OUT = os.path.join(MODEL_DIR, "best_model.keras")

TARGET_REG = "Delivery_Time_min"
TARGET_CLASS = "Delivery_Class"

NUM_COLS = ["Distance_km", "Preparation_Time_min", "Courier_Experience_yrs", "Is_RushHour"]
CAT_COLS = ["Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type"]

TRAIN_CSV = "data/train/train.csv"
VAL_CSV = "data/validation/validation.csv"
TEST_CSV = "data/test/test.csv"

RANDOM_STATE = 42


# -----------------------------
# Utilities
# -----------------------------
def set_seeds(seed: int = 42):
    np.random.seed(seed)
    tf.random.set_seed(seed)


def load_split(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Lipsește {path}")

    df = pd.read_csv(path)

    needed = set(NUM_COLS + CAT_COLS + [TARGET_REG, TARGET_CLASS])
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"În {path} lipsesc coloane: {missing}")

    X_df = df[NUM_COLS + CAT_COLS].copy()

    # y pentru minute
    y_minutes = df[TARGET_REG].astype("float32").to_numpy()

    # y pentru clasă (0/1/2)
    y_class = df[TARGET_CLASS].astype("int32").to_numpy()

    return X_df, y_minutes, y_class


def compute_class_weights(y: np.ndarray) -> dict:
    """
    Greutăți invers proporționale cu frecvența claselor.
    Ajută la class imbalance (ex: clasa 2 rară).
    """
    classes, counts = np.unique(y, return_counts=True)
    total = counts.sum()
    weights = {int(c): float(total / (len(classes) * cnt)) for c, cnt in zip(classes, counts)}
    return weights


def make_sample_weights(y_class: np.ndarray, class_weights: dict) -> np.ndarray:
    """
    Construiește sample_weight pentru fiecare exemplu, pe baza clasei lui.
    Folosim asta deoarece Keras NU suportă class_weight pentru modele multi-output.
    """
    return np.array([class_weights[int(c)] for c in y_class], dtype="float32")


def ensure_dirs():
    os.makedirs(MODEL_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)


def to_dense_if_needed(X):
    """
    OneHotEncoder poate produce sparse matrix. TensorFlow preferă dense.
    Pentru 7700x22 e foarte mic -> conversia e sigură.
    """
    if hasattr(X, "toarray"):
        return X.toarray().astype("float32")
    return X.astype("float32")


# -----------------------------
# Main train
# -----------------------------
def main():
    set_seeds(RANDOM_STATE)
    ensure_dirs()

    # 1) Load preprocessing pipeline (fit pe train, salvat anterior)
    if not os.path.exists(PIPE_PATH):
        raise FileNotFoundError(
            f"Nu găsesc {PIPE_PATH}. Rulează mai întâi: python src/preprocessing/fit_preprocessing_pipeline.py"
        )
    pipe = joblib.load(PIPE_PATH)

    # 2) Load splits
    X_train_df, y_train_min, y_train_cls = load_split(TRAIN_CSV)
    X_val_df, y_val_min, y_val_cls = load_split(VAL_CSV)
    X_test_df, y_test_min, y_test_cls = load_split(TEST_CSV)

    # 3) Transform using SAME pipeline
    X_train = to_dense_if_needed(pipe.transform(X_train_df))
    X_val = to_dense_if_needed(pipe.transform(X_val_df))
    X_test = to_dense_if_needed(pipe.transform(X_test_df))

    input_dim = X_train.shape[1]
    print(f"✓ Transformed shapes: train={X_train.shape}, val={X_val.shape}, test={X_test.shape}")

    # 4) Build multitask model (minute + class)
    model = build_multitask_model(input_dim=input_dim, n_classes=3)

    # 5) Handle class imbalance via sample_weight for 'class' head
    class_weights = compute_class_weights(y_train_cls)
    sw_train_class = make_sample_weights(y_train_cls, class_weights)
    sw_val_class = make_sample_weights(y_val_cls, class_weights)

    # 6) Callbacks (stabil + reproductibil)
    callbacks = [
        tf.keras.callbacks.ModelCheckpoint(
             BEST_MODEL_OUT,
             monitor="val_minutes_mae",
             mode="min",
             save_best_only=True,
             save_weights_only=False,
              verbose=1
        ),
        tf.keras.callbacks.EarlyStopping(
            monitor="val_minutes_mae",
            mode="min",
            patience=8,
            restore_best_weights=True,
            verbose=1
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
             monitor="val_minutes_mae",
             mode="min",
             factor=0.5,
             patience=3,
             min_lr=1e-5,
             verbose=1
        )
    ]

    # 7) Train (minim 10 epoci; noi permitem până la 40 cu early stopping)
    # sample_weight: un vector de 1.0 pentru minutes, și vectorul ponderat pentru class
    sw_train_minutes = np.ones(len(y_train_min), dtype="float32")
    sw_val_minutes = np.ones(len(y_val_min), dtype="float32")

    history = model.fit(
       X_train,
     [y_train_min, y_train_cls],                     # <-- LISTĂ, nu dict
     sample_weight=[sw_train_minutes, sw_train_class],  # <-- LISTĂ, nu dict
     validation_data=(
         X_val,
         [y_val_min, y_val_cls],                     # <-- LISTĂ
         [sw_val_minutes, sw_val_class],             # <-- LISTĂ
     ),
     epochs=40,
     batch_size=32,
     callbacks=callbacks,
     verbose=1
    )


    os.makedirs("docs", exist_ok=True)

    history_df = pd.DataFrame(history.history)
    history_df.to_csv("docs/training_history.csv", index=False)
    print("✓ training_history.csv salvat în docs/")
    history_df.to_csv("results/training_history.csv", index=False)
    print("✓ training_history.csv salvat în results/")

    # 8) Save final model
    model.save(MODEL_OUT)

    # 9) Evaluate on test
    pred_minutes, pred_class_probs = model.predict(X_test, verbose=0)
    pred_minutes = pred_minutes.reshape(-1)
    pred_class = pred_class_probs.argmax(axis=1)

    mae = float(mean_absolute_error(y_test_min, pred_minutes))
    rmse = float(np.sqrt(mean_squared_error(y_test_min, pred_minutes)))
    acc = float(accuracy_score(y_test_cls, pred_class))
    f1_macro = float(f1_score(y_test_cls, pred_class, average="macro"))

    report_dict = classification_report(y_test_cls, pred_class, output_dict=True)

    # 10) Save results
    with open(os.path.join(RESULTS_DIR, "train_history.json"), "w", encoding="utf-8") as f:
        json.dump(history.history, f, indent=2, ensure_ascii=False)

    with open(os.path.join(RESULTS_DIR, "test_metrics.json"), "w", encoding="utf-8") as f:
        json.dump({
            "input_dim": int(input_dim),
            "class_distribution_train": {str(k): float(v) for k, v in zip(*np.unique(y_train_cls, return_counts=True))},
            "class_weights_used_for_sample_weight": class_weights,
            "test_mae_minutes": mae,
            "test_rmse_minutes": rmse,
            "test_accuracy_class": acc,
            "test_f1_macro_class": f1_macro,
            "classification_report": report_dict,
            "saved_model": MODEL_OUT,
            "best_model": BEST_MODEL_OUT
        }, f, indent=2, ensure_ascii=False)

    print("\n✓ Training done.")
    print(f"Saved final model: {MODEL_OUT}")
    print(f"Saved best model:  {BEST_MODEL_OUT}")
    print(f"TEST MAE (minutes): {mae:.3f}")
    print(f"TEST RMSE (minutes): {rmse:.3f}")
    print(f"TEST Accuracy (class): {acc:.3f}")
    print(f"TEST F1 macro (class): {f1_macro:.3f}")


if __name__ == "__main__":
    main()

#python -m src.neural_network.train