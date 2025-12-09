"""
Modul 1 – Data Acquisition 
Acest script genereaza date sintetice pentru livrarea de mancare, 
pentru a asigura contributia personala de minimum 40% din datasetul 
final. 
Genereaza un fisier: data/generated/generated_deliveries.csv cu aceleasi
coloane ca datasetul original: 
    Distance_km, Weather, 
    Traffic_Level, 
    Time_of_Day, 
    Vehicle_Type, 
    Preparation_Time_min, 
    Courier_Experience_yrs, 
    Delivery_Time_min
"""

import numpy as np
import pandas as pd
import os


def generate_synthetic_deliveries(n_rows: int = 700) -> pd.DataFrame:
    """Generează n_rows livrări sintetice, realist simulate."""

    np.random.seed(42)  # reproducibilitate

    # ----------------------------
    # Generare variabile
    # ----------------------------
    distance = np.random.uniform(0.5, 20.0, size=n_rows)
    prep_time = np.random.randint(5, 40, size=n_rows)
    exp_years = np.random.randint(0, 11, size=n_rows)

    weather = np.random.choice(["Clear", "Rainy", "Foggy", "Snowy"], size=n_rows)
    traffic = np.random.choice(["Low", "Medium", "High"], size=n_rows)
    time_of_day = np.random.choice(["Morning", "Afternoon", "Evening", "Night"], size=n_rows)
    vehicle = np.random.choice(["Bike", "Scooter", "Car"], size=n_rows)

    # ----------------------------
    # Model fizic simplificat pentru timpul de livrare
    # ----------------------------
    speed_factor = np.random.uniform(2.0, 4.0, size=n_rows)  # minute per km
    base_time = distance * speed_factor

    prep_effect = prep_time * 0.8

    traffic_penalty = np.where(traffic == "High", 8,
                        np.where(traffic == "Medium", 4, 0))

    weather_penalty = np.where(weather == "Snowy", 10,
                        np.where(weather == "Rainy", 5, 0))

    vehicle_factor = np.where(vehicle == "Bike", 1.1,
                       np.where(vehicle == "Car", 1.05, 1.0))

    experience_bonus = np.clip((10 - exp_years) * 0.5, 0, None)

    delivery_time = (
        base_time * vehicle_factor +
        prep_effect +
        traffic_penalty +
        weather_penalty +
        experience_bonus
    ).astype(int)

    # ----------------------------
    # Construire DataFrame
    # ----------------------------
    df = pd.DataFrame({
        "Distance_km": distance.round(2),
        "Weather": weather,
        "Traffic_Level": traffic,
        "Time_of_Day": time_of_day,
        "Vehicle_Type": vehicle,
        "Preparation_Time_min": prep_time,
        "Courier_Experience_yrs": exp_years,
        "Delivery_Time_min": delivery_time
    })

    return df


def main():
    n_rows = 700
    df_generated = generate_synthetic_deliveries(n_rows)

    # Folderul unde salvăm
    output_dir = os.path.join("data", "generated")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "generated_deliveries.csv")
    df_generated.to_csv(output_path, index=False)

    print(f"[OK] Am generat {n_rows} rânduri sintetice în: {output_path}")


if __name__ == "__main__":
    main()
