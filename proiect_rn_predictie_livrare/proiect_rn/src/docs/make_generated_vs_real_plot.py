import os
import pandas as pd
import matplotlib.pyplot as plt

REAL_PATH = "data/raw/Food_Delivery_Times.csv"
GEN_PATH = "data/generated/generated_data.csv"
OUT_PATH = "docs/generated_vs_real.png"

NUM_COLS = ["Delivery_Time_min", "Distance_km", "Preparation_Time_min", "Courier_Experience_yrs"]
CAT_COLS = ["Traffic_Level", "Weather", "Time_of_Day", "Vehicle_Type"]

def main():
    if not os.path.exists(REAL_PATH):
        raise FileNotFoundError(f"Lipsește {REAL_PATH}")
    if not os.path.exists(GEN_PATH):
        raise FileNotFoundError(f"Lipsește {GEN_PATH}. Rulează generatorul mai întâi.")

    real = pd.read_csv(REAL_PATH)
    gen = pd.read_csv(GEN_PATH)

    os.makedirs("docs", exist_ok=True)

    # Figure mare, cu mai multe ploturi
    fig = plt.figure(figsize=(16, 14))

    # ---- NUMERICE: histograme suprapuse (cu densitate)
    for i, col in enumerate(NUM_COLS, start=1):
        ax = plt.subplot(3, 2, i)
        ax.hist(real[col].dropna(), bins=30, density=True, alpha=0.5, label="Real")
        ax.hist(gen[col].dropna(), bins=30, density=True, alpha=0.5, label="Generated")
        ax.set_title(f"Distribuție: {col}")
        ax.set_xlabel(col)
        ax.set_ylabel("Densitate")
        ax.legend()

    # ---- CATEGORICE: bar chart pe proporții (Real vs Generated)
    # Punem 2 grafice categoriale (comasate) în ultimele 2 subplot-uri
    # Traffic + Weather într-un ax, Time_of_Day + Vehicle în alt ax
    def plot_cat(ax, col):
        real_p = real[col].value_counts(normalize=True)
        gen_p = gen[col].value_counts(normalize=True)
        idx = sorted(set(real_p.index).union(set(gen_p.index)))

        real_vals = [real_p.get(k, 0.0) for k in idx]
        gen_vals = [gen_p.get(k, 0.0) for k in idx]

        x = range(len(idx))
        w = 0.4
        ax.bar([v - w/2 for v in x], real_vals, width=w, label="Real")
        ax.bar([v + w/2 for v in x], gen_vals, width=w, label="Generated")
        ax.set_title(f"Proporții: {col}")
        ax.set_xticks(list(x))
        ax.set_xticklabels(idx, rotation=20, ha="right")
        ax.set_ylabel("Proporție")
        ax.legend()

    ax5 = plt.subplot(3, 2, 5)
    plot_cat(ax5, "Traffic_Level")

    ax6 = plt.subplot(3, 2, 6)
    plot_cat(ax6, "Weather")

    plt.tight_layout()
    plt.savefig(OUT_PATH, dpi=200)
    plt.close()

    print(f"✓ Saved: {OUT_PATH}")

if __name__ == "__main__":
    main()
