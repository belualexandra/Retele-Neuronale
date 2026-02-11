# src/app/preprocess_runtime.py
"""
Preprocess Runtime (Etapa 5) — SINGLE SOURCE OF TRUTH for preprocessing

Scop:
- Să asigure PREPROCESARE IDENTICĂ între:
  (1) training (Etapa 5) și (2) aplicația web (Streamlit).
- Pipeline-ul este salvat și încărcat din:
    config/preprocessing_params.pkl   (cerut în README)
- Nu face "fit" în aplicația web (ca să evităm mismatch / leakage).

Conține:
- fit_and_save_pipeline(train_df): folosit o singură dată pe TRAIN (offline).
- load_pipeline(): folosit în aplicație + la inferență.
- build_input_dataframe(...): helper pentru construirea unui DataFrame compatibil.
- transform(pipe, df): transformă DataFrame -> matrix numerică pentru model.

IMPORTANT:
- Fit doar pe TRAIN (data/train/train.csv).
- La inferență se folosește doar load_pipeline() + transform().
"""

from __future__ import annotations

import os
import joblib
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline


# -----------------------------
# Paths
# -----------------------------
PIPE_PATH = "config/preprocessing_params.pkl"          # cerut de README
PIPE_BACKUP_PATH = "config/preprocessing_pipeline.joblib"  # opțional, backup


# -----------------------------
# Columns (TREBUIE să coincidă cu Etapa 3/5)
# -----------------------------
NUM_COLS = ["Distance_km", "Preparation_Time_min", "Courier_Experience_yrs", "Is_RushHour"]
CAT_COLS = ["Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type"]

ALL_COLS = NUM_COLS + CAT_COLS


# -----------------------------
# Fit + Save (offline, o singură dată pe TRAIN)
# -----------------------------
def fit_and_save_pipeline(train_df: pd.DataFrame) -> Pipeline:
    """
    Fit pe setul de TRAIN și salvează pipeline-ul.
    A se rula DOAR offline (nu în UI), pentru a evita mismatch train/inference.

    Parametri:
        train_df: DataFrame care conține cel puțin coloanele din ALL_COLS.

    Return:
        Pipeline fitted (sklearn)
    """
    _validate_columns(train_df, ALL_COLS)

    pre = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUM_COLS),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CAT_COLS),
        ],
        remainder="drop",
    )

    pipe = Pipeline([("pre", pre)])
    pipe.fit(train_df[ALL_COLS])

    os.makedirs("config", exist_ok=True)
    joblib.dump(pipe, PIPE_PATH)
    # backup (opțional)
    joblib.dump(pipe, PIPE_BACKUP_PATH)

    return pipe


# -----------------------------
# Load (folosit în aplicație)
# -----------------------------
def load_pipeline() -> Pipeline:
    """
    Încarcă pipeline-ul salvat în config/preprocessing_params.pkl.
    """
    if not os.path.exists(PIPE_PATH):
        raise FileNotFoundError(
            f"Nu există {PIPE_PATH}. "
            "Rulează mai întâi pipeline-ul offline (Etapa 5): "
            "python src/preprocessing/fit_preprocessing_pipeline.py"
        )
    return joblib.load(PIPE_PATH)


# -----------------------------
# Transform
# -----------------------------
def transform(pipe: Pipeline, df: pd.DataFrame) -> np.ndarray:
    """
    Transformă DataFrame-ul de input în matrice numerică (float32),
    folosind pipeline-ul încărcat.

    Return:
        np.ndarray shape (n_samples, n_features)
    """
    _validate_columns(df, ALL_COLS)

    X = pipe.transform(df[ALL_COLS])

    # OneHotEncoder poate întoarce sparse matrix -> convertim la dense (safe pentru dimensiuni mici)
    if hasattr(X, "toarray"):
        X = X.toarray()

    return X.astype("float32")


# -----------------------------
# Helper: construirea inputului pentru UI
# -----------------------------
def build_input_dataframe(
    distance_km: float,
    preparation_time_min: int,
    courier_experience_yrs: int,
    weather: str,
    traffic_level: str,
    time_of_day: str,
    vehicle_type: str,
) -> pd.DataFrame:
    """
    Creează un DataFrame cu exact coloanele așteptate de pipeline.
    Folosește aceeași logică pentru Is_RushHour ca în feature_engineering (Morning/Evening).
    """
    is_rush = 1 if time_of_day in ["Morning", "Evening"] else 0

    row = {
        "Distance_km": float(distance_km),
        "Preparation_Time_min": int(preparation_time_min),
        "Courier_Experience_yrs": int(courier_experience_yrs),
        "Is_RushHour": int(is_rush),
        "Weather": str(weather),
        "Traffic_Level": str(traffic_level),
        "Time_of_Day": str(time_of_day),
        "Vehicle_Type": str(vehicle_type),
    }
    return pd.DataFrame([row])


# -----------------------------
# Internal validation
# -----------------------------
def _validate_columns(df: pd.DataFrame, required_cols: list[str]) -> None:
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(
            f"Lipsesc coloane necesare pentru preprocesare: {missing}\n"
            f"Coloane prezente: {list(df.columns)}"
        )
