from flask import Flask, request
import joblib
import tensorflow as tf
import pandas as pd
import os

app = Flask(__name__)

# -------------------------------------------------
# 1. Încărcăm preprocessor + modelul antrenat
# -------------------------------------------------

PREPROCESSOR_PATH = "data/processed/preprocessor.pkl"
MODEL_PATH = "src/neural_network/models/delivery_time_model.keras"

if not os.path.exists(PREPROCESSOR_PATH):
    raise FileNotFoundError(f"Lipsește preprocessor-ul la {PREPROCESSOR_PATH}")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Lipsește modelul RN la {MODEL_PATH}")

preprocessor = joblib.load(PREPROCESSOR_PATH)
model = tf.keras.models.load_model(MODEL_PATH)


@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Food Delivery Time Predictor</title>
        <style>
            body {
                background: #f4f4f9;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                width: 420px;
            }
            h2 {
                text-align: center;
                color: #333;
            }
            label {
                font-weight: bold;
                margin-top: 10px;
                display: block;
            }
            input, select {
                width: 100%;
                padding: 10px;
                margin-top: 5px;
                border-radius: 6px;
                border: 1px solid #ccc;
            }
            button {
                width: 100%;
                padding: 12px;
                margin-top: 20px;
                background: #5568fe;
                border: none;
                color: white;
                font-size: 16px;
                border-radius: 6px;
                cursor: pointer;
            }
            button:hover {
                background: #4052d6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Predictie Timp Livrare</h2>
            <form action="/predict" method="post">

                <label>Distanta (km)</label>
                <input type="number" name="distance" step="0.1" required>

                <label>Timp Preparare (min)</label>
                <input type="number" name="prep" step="1" required>

                <label>Experienta Curier (ani)</label>
                <input type="number" name="exp" step="1" required>

                <label>Vreme</label>
                <select name="weather">
                    <option>Clear</option>
                    <option>Rainy</option>
                    <option>Foggy</option>
                    <option>Snowy</option>
                </select>

                <label>Trafic</label>
                <select name="traffic">
                    <option>Low</option>
                    <option>Medium</option>
                    <option>High</option>
                </select>

                <label>Momentul zilei</label>
                <select name="time_of_day">
                    <option>Morning</option>
                    <option>Afternoon</option>
                    <option>Evening</option>
                    <option>Night</option>
                </select>

                <label>Vehicul</label>
                <select name="vehicle">
                    <option>Bike</option>
                    <option>Scooter</option>
                    <option>Car</option>
                </select>

                <button type="submit">Calculeaza</button>
            </form>
        </div>
    </body>
    </html>
    """


@app.route("/predict", methods=["POST"])
def predict():
    # 1. Colectăm datele
    data = {
        "Distance_km": [float(request.form["distance"])],
        "Preparation_Time_min": [float(request.form["prep"])],
        "Courier_Experience_yrs": [float(request.form["exp"])],
        "Weather": [request.form["weather"]],
        "Traffic_Level": [request.form["traffic"]],
        "Time_of_Day": [request.form["time_of_day"]],
        "Vehicle_Type": [request.form["vehicle"]],
    }

    df = pd.DataFrame(data)

    # 2. Preprocesăm cu același preprocessor folosit la antrenare
    X = preprocessor.transform(df)

    # 3. Modelul face predicția
    prediction = model.predict(X)[0][0]
    prediction = round(float(prediction), 2)

    # 4. Returnăm rezultatul frumooos
    return f"""
    <html>
    <body style='font-family: Arial; background:#f4f4f9; padding:40px;'>
        <div style='background:white; padding:25px; border-radius:10px; max-width:400px; margin:auto;
                    text-align:center; box-shadow:0 4px 15px rgba(0,0,0,0.1);'>
            <h2>Rezultatul Predicției</h2>

            <p><b>Timp estimat de livrare:</b> {prediction} minute</p>

            <br>
            <a href="/" 
               style='padding:10px 20px; background:#5568fe; color:white; text-decoration:none; 
                      border-radius:6px;'>Înapoi</a>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    print("Interfața rulează pe http://127.0.0.1:5000")
    app.run(debug=True)
