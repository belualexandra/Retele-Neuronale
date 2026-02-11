import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# --- CONFIGURARE ---
MODEL_PATH = "models/best_model.keras"
PIPELINE_PATH = "config/preprocessing_params.pkl"
TEST_DATA_PATH = "data/test/test.csv"
OUT_PATH = "docs/results/example_predictions.png"

CLASS_NAMES = {0: "Fast (<40 min)", 1: "Medium (40-70 min)", 2: "Slow (>70 min)"}

def generate_grid():
    if not os.path.exists(TEST_DATA_PATH):
        print(f"❌ Nu am găsit {TEST_DATA_PATH}")
        return
    
    df = pd.read_csv(TEST_DATA_PATH)
    model = load_model(MODEL_PATH)
    pipeline = joblib.load(PIPELINE_PATH)

    # 1. Pregătire date și Predicție
    X_raw = df.drop(columns=["Delivery_Time_min", "Delivery_Class"])
    X_proc = pipeline.transform(X_raw)

    print(" Rulez inferența pe tot setul de test...")
    pred_min_raw, pred_class_probs = model.predict(X_proc, verbose=0)
    pred_min = pred_min_raw.flatten()
    pred_class = np.argmax(pred_class_probs, axis=1)

    y_true_class = df["Delivery_Class"].values
    y_true_min = df["Delivery_Time_min"].values

    # 2. SELECȚIE
    abs_errors = np.abs(y_true_min - pred_min)
    
    best_50_idx = np.argsort(abs_errors)[:50]

   
    is_wrong = (pred_class[best_50_idx] != y_true_class[best_50_idx])
    
    wrong_in_best = best_50_idx[is_wrong]
    right_in_best = best_50_idx[~is_wrong]

    n_wrong = min(len(wrong_in_best), 3)
    n_right = 9 - n_wrong

    # Selecție finală
    np.random.seed(42)
    sel_idx = np.concatenate([
        np.random.choice(right_in_best, n_right, replace=False),
        np.random.choice(wrong_in_best, n_wrong, replace=False) if n_wrong > 0 else []
    ])
    np.random.shuffle(sel_idx)

    # 3. Vizualizare Grid
    fig, axes = plt.subplots(3, 3, figsize=(18, 14))
    axes = axes.flatten()
    fig.suptitle("Analiză de Precizie: Exemple cu eroare minimă de timp (MAE)", fontsize=20, fontweight='bold')

    for i, idx in enumerate(sel_idx):
        ax = axes[i]
        row = df.iloc[idx]
        
        # Date pentru afișare
        order_id = int(row['Order_ID'])
        dist = row['Distance_km']
        vreme = row['Weather']
        trafic = row['Traffic_Level']
        vehicul = row['Vehicle_Type']
        exp = int(row['Courier_Experience_yrs'])
        prep = row['Preparation_Time_min']
        
        t_real = y_true_min[idx]
        t_pred = pred_min[idx]
        mae = abs_errors[idx]
        
        c_real = CLASS_NAMES[y_true_class[idx]]
        c_pred = CLASS_NAMES[pred_class[idx]]
        
        is_ok = (y_true_class[idx] == pred_class[idx])
        color = "#2e7d32" if is_ok else "#c62828"

        ax.set_title(f"{'✅' if is_ok else '❌'} Order ID: {order_id}", fontsize=14, fontweight='bold', color=color)
        
        input_txt = (f"📍 {dist}km | 🚦 {trafic} | ☁️ {vreme}\n"
                     f"🚲 {vehicul} | 👨‍🍳 {prep}m prep | 🏅 Exp: {exp} ani")
        
        res_txt = (f"Real: {t_real:.1f} min ({c_real})\n"
                   f"Pred: {t_pred:.1f} min ({c_pred})\n"
                   f"MAE: {mae:.2f} min")

        ax.text(0.05, 0.7, input_txt, transform=ax.transAxes, fontsize=10.5, verticalalignment='top',
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9))
        
        bg_color = "#f1f8e9" if is_ok else "#fff9c4" # Galben pal pentru erori de graniță
        ax.text(0.05, 0.38, res_info := res_txt, transform=ax.transAxes, fontsize=11, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.4", facecolor=bg_color, edgecolor=color))

        ax.set_xticks([]); ax.set_yticks([])
        ax.set_facecolor("#fcfcfc")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    plt.savefig(OUT_PATH, dpi=150)
    print(f" Grid de precizie salvat în: {OUT_PATH}")

if __name__ == "__main__":
    generate_grid()