import joblib
import tensorflow as tf
from tensorflow.keras import layers, models
import os

# ------------------------------
# 1. Load processed data
# ------------------------------
X_train = joblib.load("data/train/X_train_prep.pkl")
y_train = joblib.load("data/train/y_train.pkl")

X_val = joblib.load("data/validation/X_val_prep.pkl")
y_val = joblib.load("data/validation/y_val.pkl")

print("Date încărcate:")
print("Train:", X_train.shape, "Val:", X_val.shape)

# ------------------------------
# 2. Build model
# ------------------------------
model = models.Sequential([
    layers.Input(shape=(X_train.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)
])

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

model.summary()

# ------------------------------
# 3. Train model
# ------------------------------
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=25,
    batch_size=32
)

# ------------------------------
# 4. Save model
# ------------------------------
output_dir = "src/neural_network/models"
os.makedirs(output_dir, exist_ok=True)

model.save(os.path.join(output_dir, "delivery_time_model.keras"))

print("\nModel salvat cu succes în: src/neural_network/models/delivery_time_model.keras")
