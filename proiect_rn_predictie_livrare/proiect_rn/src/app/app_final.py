import os
import numpy as np
import pandas as pd
import streamlit as st
from tensorflow import keras

from src.app.preprocess_runtime import load_pipeline, transform, build_input_dataframe

# ---------------- Config ----------------
PIPE_PATH = "config/preprocessing_params.pkl"
BEST_MODEL_PATH = "models/best_model.keras"
TRAINED_MODEL_PATH = "models/trained_model.keras"

st.set_page_config(
    page_title="Delivery Time Predictor",
    page_icon="🛵",
    layout="wide",
)

# ---------------- Minimal premium CSS ----------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700;800&display=swap');

    /* 1. TEXT NEGRU PROFESIONAL */
    html, body, [class*="css"], .stMarkdown, label, h1, h2, h3 {
        font-family: 'Poppins', sans-serif;
        color: #1a1a1a !important; 
    }

    /* 2. FUNDAL INTELIGENT */
    .stApp {
        background-image: 
            linear-gradient(to bottom, rgba(255, 248, 225, 0.6) 0%, rgba(255, 243, 200, 0.9) 60%, #fff1e1 100%),
            url('https://gadget.ro/wp-content/uploads/2022/08/food-delivery.jpg');
        background-size: 100% auto, cover;
        background-repeat: no-repeat;
        background-position: top center;
        background-attachment: fixed;
    }

    /* 3. CHENAR PENTRU TITLU (Header Box) */
    .header-container {
        background: rgba(255, 255, 255, 0.9);
        border: 2px solid #ffb74d; /* Bordură portocalie caldă */
        border-radius: 30px;
        padding: 2rem;
        text-align: center;
        margin: 2rem auto;
        max-width: 900px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    }

    /* 4. CARDURI PENTRU DATE */
    .clean-card {
        background-color: #ffffff;
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid #ffe0b2;
        margin-bottom: 1rem;
    }

    .section-title {
        font-weight: 800;
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
        color: #e65100 !important;
    }

    /* 5. REZULTAT (Portocaliu) */
    .result-box {
        background: linear-gradient(135deg, #ff6f00, #ff8f00);
        padding: 2.5rem;
        border-radius: 24px;
        text-align: center;
        color: white !important;
        box-shadow: 0 10px 25px rgba(255, 111, 0, 0.4);
    }

    .time-value {
        font-size: 4.5rem;
        font-weight: 900;
        margin: 0;
        line-height: 1;
        color: white !important;
    }

    /* 6. BUTON */
    .stButton>button {
        width: 100%;
        background: #000000;
        color: white !important;
        border-radius: 14px;
        padding: 1rem;
        font-weight: 700;
        font-size: 1.1rem;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background: #333333;
        transform: translateY(-2px);
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- Loaders (logic unchanged) ----------------
@st.cache_resource
def load_model():
    if os.path.exists(BEST_MODEL_PATH):
        return keras.models.load_model(BEST_MODEL_PATH)
    if os.path.exists(TRAINED_MODEL_PATH):
        return keras.models.load_model(TRAINED_MODEL_PATH)
    raise FileNotFoundError("Modelul antrenat nu a fost găsit.")

@st.cache_resource
def load_pipe():
    if not os.path.exists(PIPE_PATH):
        raise FileNotFoundError("Pipeline-ul de preprocesare nu a fost găsit.")
    return load_pipeline()

LABELS = {0: "Rapid", 1: "Mediu", 2: "Încet"}

# ---------------- App ----------------
def main():
    # Header
    st.markdown("# 🛵 Delivery Time Predictor")
    st.markdown(
        "<div class='label'>Estimare inteligentă a timpului de livrare</div>",
        unsafe_allow_html=True,
    )

    # Load ML
    try:
        pipe = load_pipe()
        model = load_model()
    except FileNotFoundError as e:
        st.error(str(e))
        st.stop()

    st.write("")

    # Layout principal
    left, right = st.columns([1, 1.2], vertical_alignment="top")

    # -------- INPUT (PRIM-PLAN) --------
    with left:
        st.markdown("### 🧾 Configurare comandă")
        st.markdown('<div class="card">', unsafe_allow_html=True)

        distance = st.number_input("Distanță (km)", 0.1, 50.0, 5.0, 0.1)
        prep = st.number_input("Timp preparare (minute)", 1, 240, 15, 1)
        exp = st.number_input("Experiență curier (ani)", 0, 30, 2, 1)

        weather = st.selectbox("Vreme", ["Clear", "Rainy", "Foggy", "Windy", "Snowy"])
        traffic = st.selectbox("Trafic", ["Low", "Medium", "High"])
        tod = st.selectbox("Momentul zilei", ["Morning", "Afternoon", "Evening", "Night"])
        veh = st.selectbox("Tip vehicul", ["Bike", "Scooter", "Car"])

        st.write("")
        predict = st.button("🚀 Estimează timpul de livrare", use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # -------- OUTPUT (CLAR, CURAT) --------
    with right:
        st.markdown("### 📈 Rezultat estimare")
        st.markdown('<div class="card">', unsafe_allow_html=True)

        if not predict:
            st.info("Completează datele și apasă butonul pentru a obține estimarea.")
        else:
            x_df = build_input_dataframe(
                distance_km=distance,
                preparation_time_min=prep,
                courier_experience_yrs=exp,
                weather=weather,
                traffic_level=traffic,
                time_of_day=tod,
                vehicle_type=veh,
            )

            X = transform(pipe, x_df)

            minutes_pred, class_probs = model.predict(X, verbose=0)

            minutes = max(0.0, float(minutes_pred[0][0]))
            probs = class_probs[0]
            cls = int(np.argmax(probs))

            st.success(f"⏱️ **{minutes:.1f} minute**")
            st.markdown(f"**Nivel livrare:** {LABELS.get(cls)}")
            st.caption(f"Grad de încredere: {max(probs):.2f}")

        st.markdown("</div>", unsafe_allow_html=True)

    # Footer discret
    st.write("")
    st.caption("© Delivery Time Predictor • aplicație demonstrativă ML")

if __name__ == "__main__":
    main()
