import pandas as pd
import matplotlib.pyplot as plt
import os

HISTORY_PATH = "docs/training_history.csv"
OUT_PATH = "docs/loss_curve.png"

def main():
    if not os.path.exists(HISTORY_PATH):
        raise FileNotFoundError("Nu există training_history.csv. Rulează training-ul cu salvare history.")

    df = pd.read_csv(HISTORY_PATH)

    plt.figure(figsize=(8, 5))
    plt.plot(df["loss"], label="Train loss")
    plt.plot(df["val_loss"], label="Validation loss")

    plt.xlabel("Epocă")
    plt.ylabel("Loss")
    plt.title("Evoluția loss și val_loss în timpul antrenării")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(OUT_PATH, dpi=200)
    plt.close()

    print(f"✓ Grafic salvat în: {OUT_PATH}")

if __name__ == "__main__":
    main()
