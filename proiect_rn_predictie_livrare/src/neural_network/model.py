from __future__ import annotations
from tensorflow import keras
from tensorflow.keras import layers

def build_multitask_model(input_dim: int, n_classes: int = 3) -> keras.Model:
    """
    Model multi-task:
    - Output 1: regresie -> Delivery_Time_min (minute)
    - Output 2: clasificare -> Delivery_Class (0/1/2)

    Avantaje:
    - UI poate afișa minute (cerință practică).
    - Păstrăm și clasificarea pentru accuracy/F1 (Etapa 5).
    """
    inp = layers.Input(shape=(input_dim,), name="input_features")

    x = layers.Dense(128, activation="relu")(inp)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.25)(x)

    x = layers.Dense(64, activation="relu")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.20)(x)

    # Head regresie (minute)
    out_minutes = layers.Dense(1, activation="linear", name="minutes")(x)

    # Head clasificare (3 clase)
    out_class = layers.Dense(n_classes, activation="softmax", name="class")(x)

    model = keras.Model(inputs=inp, outputs=[out_minutes, out_class], name="DeliveryTime_Multitask_v1")

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=1e-3),
        loss={
            "minutes": "mse",
            "class": "sparse_categorical_crossentropy",
        },
        metrics={
            "minutes": ["mae"],
            "class": ["accuracy"],
        },
        loss_weights={
            "minutes": 1.0,
            "class": 0.5,   # clasificarea contează, dar minutele sunt prioritatea practică
        }
    )
    return model
