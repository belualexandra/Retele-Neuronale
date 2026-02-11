import pandas as pd
import json
import os

# 1. Definim căile către fișierele tale (acum pointing către folderul results)
file_baseline = 'results/training_history.csv'
file_optimized = 'results/training_history_compare.csv'

# 2. Verificăm dacă fișierele chiar sunt acolo
if not os.path.exists(file_baseline) or not os.path.exists(file_optimized):
    print(f" Eroare: Nu am găsit fișierele în folderul 'results/'.")
    print(f"Verifică dacă ai acolo: {file_baseline} și {file_optimized}")
    exit()

try:
    # 3. Citim datele
    print("Citim istoricul antrenamentelor din folderul results...")
    h1 = pd.read_csv(file_baseline).iloc[-1]
    h2 = pd.read_csv(file_optimized).iloc[-1]

    # 4. Generăm optimization_experiments.csv (tot în results/)
    print(" Generăm optimization_experiments.csv...")
    experiments_data = [
        {
            "Experiment": "Baseline (Etapa 5)",
            "Val_Accuracy": round(h1['val_class_accuracy'], 4),
            "Val_MAE_Minutes": round(h1['val_minutes_mae'], 2),
            "Val_Loss_Total": round(h1['val_loss'], 2),
            "Architecture": "64-32 Neurons"
        },
        {
            "Experiment": "Optimized (Etapa 6)",
            "Val_Accuracy": round(h2['val_class_accuracy'], 4),
            "Val_MAE_Minutes": round(h2['val_minutes_mae'], 2),
            "Val_Loss_Total": round(h2['val_loss'], 2),
            "Architecture": "128-64 Neurons + Dropout"
        }
    ]
    pd.DataFrame(experiments_data).to_csv('results/optimization_experiments.csv', index=False)

    # 5. Generăm final_metrics.json
    print(" Generăm final_metrics.json...")
    final_metrics = h2.to_dict()
    # Conversie formate numpy -> standard
    cleaned_metrics = {k: float(v) if hasattr(v, 'item') else v for k, v in final_metrics.items()}
    
    with open('results/final_metrics.json', 'w') as f:
        json.dump(cleaned_metrics, f, indent=4)

    print("\n Succes! Fișierele noi au fost adăugate în folderul 'results/'.")

except Exception as e:
    print(f" A apărut o eroare la procesare: {e}")