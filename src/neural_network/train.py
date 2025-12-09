"""
train.py – Lansarea procesului de antrenare (schelet)

Acest script:
- încarcă datele preprocesate
- construiește modelul folosind build_model()
- afișează sumarul rețelei neuronale
- pregătește infrastructura necesară antrenării (Etapa 5)
"""

"""
train.py – Lansarea procesului de antrenare (schelet, Etapa 4)

Acest script:
- încarcă datele preprocesate (train / validation)
- construiește modelul folosind build_model()
- afișează sumarul rețelei neuronale
- pregătește infrastructura necesară pentru Etapa 5 (antrenarea completă)
"""

import joblib
import os
from model import build_model


def main():

    # ============================================================
    # 1. DEFINIREA CĂILOR CĂTRE SETURILE DE DATE
    # ============================================================

    TRAIN_X_PATH = os.path.join("data", "train", "X_train_prep.pkl")
    TRAIN_Y_PATH = os.path.join("data", "train", "y_train.pkl")

    VAL_X_PATH = os.path.join("data", "validation", "X_val_prep.pkl")
    VAL_Y_PATH = os.path.join("data", "validation", "y_val.pkl")

    # ============================================================
    # 2. ÎNCĂRCAREA SETURILOR PREPROCESATE
    # ============================================================

    if not os.path.exists(TRAIN_X_PATH):
        raise FileNotFoundError(f"Nu s-a găsit fișierul: {TRAIN_X_PATH}")

    if not os.path.exists(TRAIN_Y_PATH):
        raise FileNotFoundError(f"Nu s-a găsit fișierul: {TRAIN_Y_PATH}")

    X_train = joblib.load(TRAIN_X_PATH)
    y_train = joblib.load(TRAIN_Y_PATH)

    print("Datele de antrenare au fost încărcate!")
    print("Dimensiune X_train:", X_train.shape)

    # VALIDATION DATA (optional în Etapa 4, obligatoriu în Etapa 5)
    if os.path.exists(VAL_X_PATH) and os.path.exists(VAL_Y_PATH):
        X_val = joblib.load(VAL_X_PATH)
        y_val = joblib.load(VAL_Y_PATH)
        print("Datele de validare au fost încărcate!")
        print("Dimensiune X_val:", X_val.shape)
    else:
        X_val = None
        y_val = None
        print("Setul de validare nu a fost găsit! (OK pentru Etapa 4)")

    # ============================================================
    # 3. CONSTRUIREA MODELULUI
    # ============================================================

    input_dim = X_train.shape[1]
    model = build_model(input_dim)

    print("\n=== Arhitectura rețelei neuronale ===")
    model.summary()

    # ============================================================
    # 4. FINAL – Pregătit pentru Etapa 5
    # ============================================================

    print("\nModelul este pregătit pentru antrenare completă în Etapa 5.")


if __name__ == "__main__":
    main()
