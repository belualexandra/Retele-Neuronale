import pandas as pd
import matplotlib.pyplot as plt
import os

# Căi implicite
DEFAULT_HISTORY_PATH = "results/training_history.csv"
OUT_PATH = "docs/results/learning_curves_final.png"

def main():
    
    possible_paths = [
        DEFAULT_HISTORY_PATH,
        "training_history.csv",
        "results/training_history_compare.csv",
        "training_history_compare.csv"
    ]
    
    active_path = None
    for p in possible_paths:
        if os.path.exists(p):
            active_path = p
            break
            
    if not active_path:
        print(" EROARE: Nu s-a găsit niciun fișier de istoric (CSV).")
        print("Asigură-te că ai rulat antrenarea și că fișierul există în folderul 'results'.")
        return

    print(f" Se citesc datele din: {active_path}")
    df = pd.read_csv(active_path)
    
    # Creare figură
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # --- GRAFIC 1: LOSS (Total) ---
    ax1.plot(df['loss'], label='Train Loss', color='#1f77b4', linewidth=2)
    ax1.plot(df['val_loss'], label='Val Loss', color='#ff7f0e', linestyle='--', linewidth=2)
    ax1.set_title('Evoluție Loss (Total)', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Epocă', fontsize=12)
    ax1.set_ylabel('Loss', fontsize=12)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # --- GRAFIC 2: ACCURACY (Classification) ---
    acc_col = 'class_accuracy' if 'class_accuracy' in df.columns else 'accuracy'
    val_acc_col = 'val_' + acc_col
    
    if acc_col in df.columns:
        ax2.plot(df[acc_col], label='Train Accuracy', color='#2ca02c', linewidth=2)
        ax2.plot(df[val_acc_col], label='Val Accuracy', color='#d62728', linestyle='--', linewidth=2)
        ax2.set_title('Evoluție Acuratețe Clasificare', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Epocă', fontsize=12)
        ax2.set_ylabel('Accuracy', fontsize=12)
        ax2.legend()
        ax2.grid(True, alpha=0.3)
    
    plt.suptitle(f"Analiza Antrenării - {len(df)} Epoci", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    # Salvare
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    plt.savefig(OUT_PATH, dpi=300)
    plt.close()
    
    print(f" Graficul final a fost salvat în: {OUT_PATH}")

if __name__ == "__main__":
    main()