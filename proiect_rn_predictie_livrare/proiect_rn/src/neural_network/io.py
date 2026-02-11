import os
from tensorflow import keras

MODEL_DIR = "models"
UNTRAINED_MODEL_PATH = os.path.join(MODEL_DIR, "untrained_model.keras")

def save_untrained_model(model: keras.Model) -> str:
    """
    Salvează modelul (neantrenat) pentru demonstrat scheletul funcțional în Etapa 4.
    """
    os.makedirs(MODEL_DIR, exist_ok=True)
    model.save(UNTRAINED_MODEL_PATH)
    return UNTRAINED_MODEL_PATH

def load_untrained_model() -> keras.Model:
    """
    Încarcă modelul (neantrenat) salvat în Etapa 4.
    """
    if not os.path.exists(UNTRAINED_MODEL_PATH):
        raise FileNotFoundError(f"Nu găsesc {UNTRAINED_MODEL_PATH}. Salvează-l întâi.")
    return keras.models.load_model(UNTRAINED_MODEL_PATH)
