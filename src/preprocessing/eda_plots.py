import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Încarcă datele reale
df = pd.read_csv("data/raw/Food_Delivery_Times.csv")

# Creează folderul pentru grafice
output_dir = "docs/datasets/eda_plots"
os.makedirs(output_dir, exist_ok=True)

print("Generez grafice EDA...")

# =========================================================
# 1) Histogram – Delivery Time
# =========================================================
plt.figure(figsize=(8,6))
plt.hist(df["Delivery_Time_min"], bins=25, color="skyblue", edgecolor="black")
plt.title("Histogram – Delivery Time")
plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Frequency")
plt.savefig(f"{output_dir}/hist_delivery_time.png")
plt.close()

# =========================================================
# 2) Histogram – Distance
# =========================================================
plt.figure(figsize=(8,6))
plt.hist(df["Distance_km"], bins=25, color="lightgreen", edgecolor="black")
plt.title("Histogram – Distance (km)")
plt.xlabel("Distance (km)")
plt.ylabel("Frequency")
plt.savefig(f"{output_dir}/hist_distance.png")
plt.close()

# =========================================================
# 3) Boxplot – Delivery Time
# =========================================================
plt.figure(figsize=(7,6))
sns.boxplot(x=df["Delivery_Time_min"], color="orange")
plt.title("Boxplot – Delivery Time")
plt.xlabel("Delivery Time (minutes)")
plt.savefig(f"{output_dir}/boxplot_delivery_time.png")
plt.close()

# =========================================================
# 4) Scatter – Distance vs Delivery Time
# =========================================================
plt.figure(figsize=(8,6))
plt.scatter(df["Distance_km"], df["Delivery_Time_min"], alpha=0.5)
plt.title("Distance vs Delivery Time")
plt.xlabel("Distance (km)")
plt.ylabel("Delivery Time (minutes)")
plt.savefig(f"{output_dir}/scatter_distance_vs_delivery.png")
plt.close()

# =========================================================
# 5) Scatter – Preparation Time vs Delivery Time
# =========================================================
plt.figure(figsize=(8,6))
plt.scatter(df["Preparation_Time_min"], df["Delivery_Time_min"], alpha=0.5, color="purple")
plt.title("Preparation Time vs Delivery Time")
plt.xlabel("Preparation Time (minutes)")
plt.ylabel("Delivery Time (minutes)")
plt.savefig(f"{output_dir}/scatter_prep_vs_delivery.png")
plt.close()

# =========================================================
# 6) Countplot – Weather
# =========================================================
plt.figure(figsize=(8,6))
sns.countplot(data=df, x="Weather", palette="Set2")
plt.title("Countplot – Weather")
plt.xlabel("Weather")
plt.ylabel("Count")
plt.savefig(f"{output_dir}/count_weather.png")
plt.close()

# =========================================================
# 7) Countplot – Traffic Level
# =========================================================
plt.figure(figsize=(8,6))
sns.countplot(data=df, x="Traffic_Level", palette="Set3")
plt.title("Countplot – Traffic Level")
plt.xlabel("Traffic Level")
plt.ylabel("Count")
plt.savefig(f"{output_dir}/count_traffic.png")
plt.close()


# =========================================================
# 8) Heatmap – Corelații între variabile numerice
# =========================================================

plt.figure(figsize=(10,8))

numeric_cols = [
    "Distance_km",
    "Preparation_Time_min",
    "Courier_Experience_yrs",
    "Delivery_Time_min"
]

corr = df[numeric_cols].corr()

sns.heatmap(corr, annot=True, cmap="Blues", linewidths=0.5)

plt.title("Correlation Heatmap – Numeric Features")
plt.savefig(f"{output_dir}/heatmap_correlations.png")
plt.close()



print("Toate graficele EDA au fost generate în docs/datasets/eda_plots/")
