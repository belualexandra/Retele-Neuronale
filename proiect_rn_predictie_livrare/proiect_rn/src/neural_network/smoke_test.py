import numpy as np
from src.neural_network.model import build_multitask_model
from src.neural_network.io import save_untrained_model, load_untrained_model

def main():
    input_dim = 22  # pune un exemplu realist, dar nu e obligatoriu
    model = build_multitask_model(input_dim=input_dim, n_classes=3)

    x = np.random.rand(4, input_dim).astype("float32")
    minutes_pred, class_probs = model.predict(x, verbose=0)

    path = save_untrained_model(model)
    model2 = load_untrained_model()
    minutes_pred2, class_probs2 = model2.predict(x, verbose=0)

    print("✓ Smoke test OK")
    print("Saved at:", path)
    print("Minutes shape:", minutes_pred.shape, "Class shape:", class_probs.shape)

if __name__ == "__main__":
    main()
