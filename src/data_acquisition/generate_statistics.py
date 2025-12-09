"""
Modul 1 – Data Acquisition
Script pentru calculul statisticilor comparative între datasetul real
și datele sintetice generate. Rezultatul este salvat în docs/data_statistics.csv.
"""

import pandas as pd
import os

# ======================================================
# Load data din structura corectă
# ======================================================

REAL_DATA_PATH = os.path.join("data", "raw", "Food_Delivery_Times.csv")
GENERATED_DATA_PATH = os.path.join("data", "generated", "generated_deliveries.csv")

if not os.path.exists(REAL_DATA_PATH):
    raise FileNotFoundError(f"Fisierul real nu exista la: {REAL_DATA_PATH}")

if not os.path.exists(GENERATED_DATA_PATH):
    raise FileNotFoundError(f"Fisierul generat nu exista la: {GENERATED_DATA_PATH}")

real = pd.read_csv(REAL_DATA_PATH)
generated = pd.read_csv(GENERATED_DATA_PATH)

# ======================================================
# Compute statistici
# ======================================================

stats = pd.DataFrame({
    "Metric": ["Mean", "Median", "Std", "Min", "Max"],
    "Real_Delivery_Time": [
        real["Delivery_Time_min"].mean(),
        real["Delivery_Time_min"].median(),
        real["Delivery_Time_min"].std(),
        real["Delivery_Time_min"].min(),
        real["Delivery_Time_min"].max()
    ],
    "Simulated_Delivery_Time": [
        generated["Delivery_Time_min"].mean(),
        generated["Delivery_Time_min"].median(),
        generated["Delivery_Time_min"].std(),
        generated["Delivery_Time_min"].min(),
        generated["Delivery_Time_min"].max()
    ]
})

# ======================================================
# Salvare în folderul docs/
# ======================================================

os.makedirs("docs", exist_ok=True)
output_path = os.path.join("docs", "data_statistics.csv")

stats.to_csv(output_path, index=False)

print(f"Statistici salvate în {output_path}")
