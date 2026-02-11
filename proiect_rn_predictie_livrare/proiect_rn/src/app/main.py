# src/app/main.py
import os
import pandas as pd
import streamlit as st
from tensorflow import keras

from src.app.preprocess_runtime import load_pipeline, transform, build_input_dataframe

PIPE_PATH = "config/preprocessing_params.pkl"
BEST_MODEL_PATH = "models/best_model.keras"
TRAINED_MODEL_PATH = "models/trained_model.keras"

st.set_page_config(page_title="Predicție livrare (Etapa 5)", layout="centered")


def load_trained_model():
    """
    În Etapa 5, aplicația NU construiește modele.
    Încarcă modelul antrenat:
      - preferă best_model.keras (cel mai bun pe validare)
      - fallback: trained_model.keras
    """
    if os.path.exists(BEST_MODEL_PATH):
        return keras.models.load_model(BEST_MODEL_PATH), BEST_MODEL_PATH

    if os.path.exists(TRAINED_MODEL_PATH):
        return keras.models.load_model(TRAINED_MODEL_PATH), TRAINED_MODEL_PATH

    raise FileNotFoundError(
        f"Nu găsesc nici {BEST_MODEL_PATH} nici {TRAINED_MODEL_PATH}.\n"
        "Rulează antrenarea: python -m src.neural_network.train"
    )


def main():
    st.title("Predicție timp livrare (SIA – Etapa 5)")
    st.caption(
        "Etapa 5: model ANTRRENAT + preprocesare identică (train vs inferență). "
        "Aplicația încarcă pipeline-ul din config și modelul din models."
    )

    # --- verificări fișiere ---
    if not os.path.exists(PIPE_PATH):
        st.error(
            f"Lipsește {PIPE_PATH}.\n"
            "Rulează: python src/preprocessing/fit_preprocessing_pipeline.py"
        )
        st.stop()

    # 1) Load preprocessing pipeline (NU FIT în UI)
    pipe = load_pipeline()

    # 2) Load trained model
    try:
        model, model_path = load_trained_model()
    except FileNotFoundError as e:
        st.error(str(e))
        st.stop()

    st.success(f"Model încărcat: `{model_path}`")
    st.info(f"Pipeline încărcat: `{PIPE_PATH}`")

    # --- input UI ---
    st.subheader("Introdu datele comenzii")
    distance = st.number_input("Distance_km", min_value=0.1, max_value=50.0, value=5.0, step=0.1)
    prep = st.number_input("Preparation_Time_min", min_value=1, max_value=120, value=15, step=1)
    exp = st.number_input("Courier_Experience_yrs", min_value=0, max_value=30, value=2, step=1)

    weather = st.selectbox("Weather", ["Clear", "Rainy", "Foggy", "Windy", "Snowy", "Unknown"])
    traffic = st.selectbox("Traffic_Level", ["Low", "Medium", "High", "Unknown"])
    tod = st.selectbox("Time_of_Day", ["Morning", "Afternoon", "Evening", "Night", "Unknown"])
    veh = st.selectbox("Vehicle_Type", ["Bike", "Scooter", "Car"])

    # 3) Build input df (coloane perfecte + Is_RushHour derivat)
    x_df = build_input_dataframe(
        distance_km=distance,
        preparation_time_min=prep,
        courier_experience_yrs=exp,
        weather=weather,
        traffic_level=traffic,
        time_of_day=tod,
        vehicle_type=veh,
    )

    # 4) Transform
    X = transform(pipe, x_df)

    if st.button("Prezice"):
        minutes_pred, class_probs = model.predict(X, verbose=0)

        minutes = float(minutes_pred[0][0])
        # safety clip (rar, dar util)
        minutes = max(0.0, minutes)

        probs = [float(p) for p in class_probs[0]]
        pred_class = int(class_probs[0].argmax())

        st.success(f"Timp estimat: **{minutes:.1f} minute**")
        st.write(f"Clasă prezisă: **{pred_class}** (0=fast, 1=medium, 2=slow)")
        st.write({"probabilities": probs})

        # Extra: interpretare simplă
        label_map = {0: "fast", 1: "medium", 2: "slow"}
        st.caption(f"Interpretare: **{label_map.get(pred_class, 'unknown')}**")


if __name__ == "__main__":
    main()
