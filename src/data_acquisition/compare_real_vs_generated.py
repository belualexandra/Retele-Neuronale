"""
Modul 1 – Data Acquisition
Script de comparare a datelor reale vs cele sintetice.
Generează TOATE graficele necesare pentru Etapa 4.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# ======================================================
# 0) LOAD DATA FROM CORRECT PROJECT STRUCTURE
# ======================================================

REAL_DATA_PATH = os.path.join("data", "raw", "Food_Delivery_Times.csv")
GENERATED_DATA_PATH = os.path.join("data", "generated", "generated_deliveries.csv")

if not os.path.exists(REAL_DATA_PATH):
    raise FileNotFoundError(f"Fisierul real nu exista la: {REAL_DATA_PATH}")

if not os.path.exists(GENERATED_DATA_PATH):
    raise FileNotFoundError(f"Fisierul generat nu exista la: {GENERATED_DATA_PATH}")

real = pd.read_csv(REAL_DATA_PATH)
generated = pd.read_csv(GENERATED_DATA_PATH)

# Ensure docs folder exists
os.makedirs("docs", exist_ok=True)

print("Datele au fost încărcate corect.\n")


# ======================================================
# 0) OFFICIAL REQUIRED GRAPH – generated_vs_real.png
# ======================================================
plt.figure(figsize=(8,6))
plt.hist(real["Delivery_Time_min"], bins=20, alpha=0.6, label="Real", density=True)
plt.hist(generated["Delivery_Time_min"], bins=20, alpha=0.6, label="Simulated", density=True)

plt.title("Comparatie Delivery_Time_min – Real vs Simulated")
plt.xlabel("Timp livrare (minute)")
plt.ylabel("Densitate")
plt.legend()
plt.tight_layout()
plt.savefig("docs/generated_vs_real.png")
plt.close()

print("Grafic oficial salvat in docs/generated_vs_real.png")


# ======================================================
# 1) Histogram Comparison (Delivery Time)
# ======================================================
plt.figure(figsize=(8,6))
plt.hist(real["Delivery_Time_min"], bins=20, alpha=0.6, label="Real", density=True)
plt.hist(generated["Delivery_Time_min"], bins=20, alpha=0.6, label="Simulated", density=True)
plt.title("Histogram: Delivery Time – Real vs Simulated")
plt.xlabel("Delivery Time (min)")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.savefig("docs/hist_delivery_time_compare.png")
plt.close()


# ======================================================
# 2) Boxplot Comparison
# ======================================================
plt.figure(figsize=(7,6))
plt.boxplot([real["Delivery_Time_min"], generated["Delivery_Time_min"]], labels=["Real", "Simulated"])
plt.title("Boxplot: Delivery Time – Real vs Simulated")
plt.ylabel("Delivery Time (min)")
plt.tight_layout()
plt.savefig("docs/boxplot_delivery_time_compare.png")
plt.close()


# ======================================================
# 3) Scatter: Distance vs Delivery Time
# ======================================================
plt.figure(figsize=(8,6))
plt.scatter(real["Distance_km"], real["Delivery_Time_min"], alpha=0.4, label="Real")
plt.scatter(generated["Distance_km"], generated["Delivery_Time_min"], alpha=0.4, label="Simulated")
plt.title("Scatter: Distance vs Delivery Time")
plt.xlabel("Distance (km)")
plt.ylabel("Delivery Time (min)")
plt.legend()
plt.tight_layout()
plt.savefig("docs/scatter_distance_delivery_compare.png")
plt.close()


# ======================================================
# 4) Bar chart – Mean comparison
# ======================================================
plt.figure(figsize=(7,6))
means = [
    real["Delivery_Time_min"].mean(),
    generated["Delivery_Time_min"].mean()
]
plt.bar(["Real", "Simulated"], means, color=["blue", "green"])
plt.title("Mean Delivery Time: Real vs Simulated")
plt.ylabel("Mean (min)")
plt.tight_layout()
plt.savefig("docs/barchart_mean_delivery_time.png")
plt.close()


# ======================================================
# 5) Scatter: Preparation Time vs Delivery Time
# ======================================================
plt.figure(figsize=(8,6))
plt.scatter(real["Preparation_Time_min"], real["Delivery_Time_min"], alpha=0.4, label="Real")
plt.scatter(generated["Preparation_Time_min"], generated["Delivery_Time_min"], alpha=0.4, label="Simulated")
plt.title("Scatter: Prep Time vs Delivery Time")
plt.xlabel("Preparation Time (min)")
plt.ylabel("Delivery Time (min)")
plt.legend()
plt.tight_layout()
plt.savefig("docs/scatter_prep_vs_delivery_compare.png")
plt.close()


# ======================================================
# 6) Scatter: Courier Experience vs Delivery Time
# ======================================================
plt.figure(figsize=(8,6))
plt.scatter(real["Courier_Experience_yrs"], real["Delivery_Time_min"], alpha=0.4, label="Real")
plt.scatter(generated["Courier_Experience_yrs"], generated["Delivery_Time_min"], alpha=0.4, label="Simulated")
plt.title("Scatter: Courier Experience vs Delivery Time")
plt.xlabel("Courier Experience (years)")
plt.ylabel("Delivery Time (min)")
plt.legend()
plt.tight_layout()
plt.savefig("docs/scatter_experience_vs_delivery_compare.png")
plt.close()


print("\n=== TOATE GRAFICELE AU FOST GENERATE ÎN FOLDERUL docs/ ===")
