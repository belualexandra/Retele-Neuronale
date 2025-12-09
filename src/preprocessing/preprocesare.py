import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import joblib
import os

print("Scriptul rulează...")

# ============================================================
# 1. CITIREA DATASETURILOR REAL + GENERAT
# ============================================================

RAW_PATH = os.path.join("data", "raw", "Food_Delivery_Times.csv")
GEN_PATH = os.path.join("data", "generated", "generated_deliveries.csv")

if not os.path.exists(RAW_PATH):
    raise FileNotFoundError(f"Dataset RAW lipsă: {RAW_PATH}")

if not os.path.exists(GEN_PATH):
    raise FileNotFoundError(f"Dataset GENERAT lipsă: {GEN_PATH}")

df_raw = pd.read_csv(RAW_PATH)
df_gen = pd.read_csv(GEN_PATH)

print("\nDate reale încărcate:", df_raw.shape)
print("Date generate încărcate:", df_gen.shape)

# ============================================================
# 2. COMBINAREA CELOR DOUĂ DATASETURI
# ============================================================

df = pd.concat([df_raw, df_gen], ignore_index=True)
print("Dataset combinat:", df.shape, "\n")

# ============================================================
# 3. DEFINIRE FEATURES / TARGET
# ============================================================

numeric_features = [
    "Distance_km",
    "Preparation_Time_min",
    "Courier_Experience_yrs"
]

categorical_features = [
    "Weather",
    "Traffic_Level",
    "Time_of_Day",
    "Vehicle_Type"
]

target = "Delivery_Time_min"

X = df[numeric_features + categorical_features]
y = df[target]

# ============================================================
# 4. ÎMPĂRȚIRE TRAIN / VAL / TEST
# ============================================================

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=42
)

# ============================================================
# 5. PREPROCESARE
# ============================================================

numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

preprocessor.fit(X_train)

X_train_prep = preprocessor.transform(X_train)
X_val_prep = preprocessor.transform(X_val)
X_test_prep = preprocessor.transform(X_test)

# ============================================================
# 6. CREARE DIRECTOARE
# ============================================================

PROC_DIR = "data/processed"
TRAIN_DIR = "data/train"
VAL_DIR = "data/validation"
TEST_DIR = "data/test"

os.makedirs(PROC_DIR, exist_ok=True)
os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(VAL_DIR, exist_ok=True)
os.makedirs(TEST_DIR, exist_ok=True)

# ============================================================
# 7. SALVARE SET COMPLET COMBINAT + PREPROCESSOR
# ============================================================

df.to_csv(os.path.join(PROC_DIR, "full_dataset.csv"), index=False)
joblib.dump(preprocessor, os.path.join(PROC_DIR, "preprocessor.pkl"))

# ============================================================
# 8. SALVARE SETURI PREPROCESATE PE FOLDERE
# ============================================================

# TRAIN
joblib.dump(X_train_prep, os.path.join(TRAIN_DIR, "X_train_prep.pkl"))
joblib.dump(y_train,      os.path.join(TRAIN_DIR, "y_train.pkl"))

# VALIDATION
joblib.dump(X_val_prep, os.path.join(VAL_DIR, "X_val_prep.pkl"))
joblib.dump(y_val,      os.path.join(VAL_DIR, "y_val.pkl"))

# TEST
joblib.dump(X_test_prep, os.path.join(TEST_DIR, "X_test_prep.pkl"))
joblib.dump(y_test,      os.path.join(TEST_DIR, "y_test.pkl"))

print("\n===============================================")
print("TOATE DATELE AU FOST PREPROCESATE ȘI SALVATE")
print("Processed  → data/processed")
print("Train      → data/train")
print("Validation → data/validation")
print("Test       → data/test")
print("===============================================\n")
