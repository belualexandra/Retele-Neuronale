import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import joblib

print("Scriptul ruleaza...")

# 1. CITIREA DATASETULUI REAL


df = pd.read_csv("Food_Delivery_Times.csv")
print("Primele 5 randuri:\n", df.head(), "\n")
print("Info dataset:\n")
print(df.info(), "\n")


# 2. DEFINIRE FEATURES / TARGET


# INPUT (X)
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

# OUTPUT (y)
target = "Delivery_Time_min"


# 3. ÎMPĂRȚIREA X ȘI y


X = df[numeric_features + categorical_features]
y = df[target]


# 4. ÎMPĂRȚIRE TRAIN / VAL / TEST


X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=42
)


# 5. PREPROCESARE (SCALARE)


numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

preprocessor.fit(X_train)

X_train_prep = preprocessor.transform(X_train)
X_val_prep   = preprocessor.transform(X_val)
X_test_prep  = preprocessor.transform(X_test)


# 6. SALVAREA SETURILOR PREPROCESATE


joblib.dump(X_train_prep, "X_train_prep.pkl")
joblib.dump(y_train, "y_train.pkl")

joblib.dump(X_val_prep, "X_val_prep.pkl")
joblib.dump(y_val, "y_val.pkl")

joblib.dump(X_test_prep, "X_test_prep.pkl")
joblib.dump(y_test, "y_test.pkl")

# Salvăm și preprocessor-ul pentru predicții
joblib.dump(preprocessor, "preprocessor.pkl")

print("Seturile pregatite au fost salvate!")