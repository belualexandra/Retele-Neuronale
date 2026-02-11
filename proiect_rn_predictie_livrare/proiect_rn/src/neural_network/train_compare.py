import os
import numpy as np
import pandas as pd
import joblib
import tensorflow as tf

from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from tensorflow.keras.models import load_model


from src.neural_network.model import build_multitask_model


PIPELINE_PATH = "config/preprocessing_pipeline.joblib"
TRAIN_CSV = "data/train/train.csv"
VAL_CSV = "data/validation/validation.csv"
TEST_CSV = "data/test/test.csv"

BEST_MODEL_PATH = "models/best_model.keras"
TRAIN_MODEL_PATH = "models/train_model.keras"   # <- cum ai cerut
RESULTS_DIR = "results"


def load_split(csv_path: str):
    df = pd.read_csv(csv_path)
    X = df.drop(columns=["Delivery_Time_min", "Delivery_Class"])
    y_minutes = df["Delivery_Time_min"].astype(np.float32).values
    y_class = df["Delivery_Class"].astype(np.int32).values
    return X, y_minutes, y_class


def main():
    os.makedirs("models", exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # 1) Load pipeline
    pipeline = joblib.load(PIPELINE_PATH)
    print("✓ Loaded preprocessing pipeline")

    # 2) Load data splits (raw) then transform with SAME pipeline
    X_train_raw, y_train_min, y_train_cls = load_split(TRAIN_CSV)
    X_val_raw, y_val_min, y_val_cls = load_split(VAL_CSV)
    X_test_raw, y_test_min, y_test_cls = load_split(TEST_CSV)

    X_train = pipeline.transform(X_train_raw)
    X_val = pipeline.transform(X_val_raw)
    X_test = pipeline.transform(X_test_raw)

    print(f"✓ Shapes: train={X_train.shape}, val={X_val.shape}, test={X_test.shape}")

    # 3) Build model
    input_dim = X_train.shape[1]
    model = build_multitask_model(input_dim=input_dim)

    # 4) Compile
    # (Păstrează exact setup-ul tău din proiect, aici e varianta tipică)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss={
            "minutes": "mse",
            "class": tf.keras.losses.SparseCategoricalCrossentropy(),
        },
        metrics={
            "minutes": [tf.keras.metrics.MeanAbsoluteError(name="mae")],
            "class": [tf.keras.metrics.SparseCategoricalAccuracy(name="accuracy")],
        },
    )

    # 5) Callbacks
    # Cheia: restore_best_weights=False ca să nu copieze best în modelul final
    early = EarlyStopping(
        monitor="val_loss",
        patience=5,
        restore_best_weights=False,  # <- IMPORTANT: așa train_model = last epoch
        verbose=1,
    )

    reduce_lr = ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=2,
        min_lr=1e-5,
        verbose=1,
    )

    ckpt = ModelCheckpoint(
        BEST_MODEL_PATH,
        monitor="val_loss",
        save_best_only=True,
        verbose=1,
    )

    # 6) Train
    history = model.fit(
        X_train,
        {"minutes": y_train_min, "class": y_train_cls},
        validation_data=(X_val, {"minutes": y_val_min, "class": y_val_cls}),
        epochs=40,
        batch_size=32,
        callbacks=[early, reduce_lr, ckpt],
        verbose=1,
    )

    # 7) Save LAST epoch model as train_model.keras
    model.save(TRAIN_MODEL_PATH)
    print(f"✓ Saved LAST-epoch model: {TRAIN_MODEL_PATH}")
    print(f"✓ Saved BEST model:      {BEST_MODEL_PATH}")

    # 8) Save training history
    hist_df = pd.DataFrame(history.history)
    hist_df.to_csv(os.path.join(RESULTS_DIR, "training_history_compare.csv"), index=False)
    print("✓ Saved history: results/training_history_compare.csv")

    # 9) Quick sanity check: compare predictions differ
    best = load_model(BEST_MODEL_PATH)
    last = load_model(TRAIN_MODEL_PATH)

    _, p_best = best.predict(X_test, verbose=0)
    _, p_last = last.predict(X_test, verbose=0)

    y_best = np.argmax(p_best, axis=1)
    y_last = np.argmax(p_last, axis=1)

    same_ratio = np.mean(y_best == y_last)
    print(f"✓ Same predicted labels ratio (best vs last): {same_ratio:.6f}")
    print("   (Dacă e < 1.0, atunci confusion matrix-urile vor diferi.)")


if __name__ == "__main__":
    main()
