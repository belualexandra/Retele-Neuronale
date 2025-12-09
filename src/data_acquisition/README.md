### README – Modul 1: Data Acquisition (Generare Date)
### Descriere generală

### Acest modul este responsabil de generarea datelor sintetice necesare pentru antrenarea rețelei neuronale utilizate în proiectul de predicție a timpului de livrare a comenzilor de mâncare.

Conform cerințelor proiectului, a fost necesară o contribuție personală de minimum 40% la datasetul final. Această contribuție este realizată printr-o simulare fizică probabilistică, care reproduce factori reali ai procesului de livrare: distanță, vreme, trafic, tipul vehiculului, experiența curierului și timpul de preparare.

### Fișierul principal al modulului:

src/data_acquisition/generate_data.py

Output generat:

data/generated/generated_deliveries.csv

1. Metoda de generare a datelor

Generarea se bazează pe simulare probabilistică realistă, construită astfel încât să reproducă distribuțiile și comportamentul fenomenelor întâlnite în livrarea reală de mâncare.

🔹 Variabile numerice (generate prin distribuții continue/discrete)

Distance_km → U(0.5, 20)

Preparation_Time_min → int U(5, 40)

Courier_Experience_yrs → int U(0, 10)

🔹 Variabile categoriale (generate prin selecție uniformă)

Weather: {Clear, Rainy, Foggy, Snowy}

Traffic_Level: {Low, Medium, High}

Time_of_Day: {Morning, Afternoon, Evening, Night}

Vehicle_Type: {Bike, Scooter, Car}

2. Formula utilizată pentru estimarea timpului de livrare

Pentru fiecare comandă, timpul final de livrare este calculat printr-un model fizic simplificat:

delivery_time =
    distance * speed_factor
  + prep_time * 0.8
  + traffic_penalty
  + weather_penalty
  + vehicle_factor
  + experience_bonus

➤ Explicații pentru termeni

| Componentă       | Descriere                    | Interval / valori               |
| ---------------- | ---------------------------- | ------------------------------- |
| speed_factor     | minute/km                    | U(2.0, 4.0)                     |
| prep_time        | timp preparare               | 5–40 min                        |
| traffic_penalty  | întârziere din trafic        | 0 / 4 / 8 min                   |
| weather_penalty  | întârziere din vreme         | 0 / 5 / 10 min                  |
| vehicle_factor   | efect vehicul                | Bike:1.1, Car:1.05, Scooter:1.0 |
| experience_bonus | curier experimentat → timp ↓ | 0–5 min                         |


Acești parametri reflectă logic și fizic comportamentul livrărilor reale.

3. Parametrii utilizați în simulare

| Parametru                 | Valoare        | Justificare                                        |
| ------------------------- | -------------- | -------------------------------------------------- |
| Număr total date generate | **700**        | reprezintă peste 40% din datasetul final           |
| Random seed               | **42**         | reproducibilitate completă                         |
| Interval distanță         | 0.5–20 km      | interval realist în majoritatea orașelor           |
| Timp preparare            | 5–40 min       | timpi obișnuiți în restaurante                     |
| Experiență curier         | 0–10 ani       | variabilitate realistă                             |
| Speed factor              | 2.0–4.0 min/km | diferențe între vehicule lente/rapide              |
| Penalizare trafic         | 0 / 4 / 8 min  | reflectă orele de vârf                             |
| Penalizare meteo          | 0 / 5 / 10 min | condițiile nefavorabile încetinesc livrarea        |
| Vehicle factor            | 1.0–1.1        | bicicleta este mai lentă, mașina blocată în trafic |
| Experience bonus          | până la -5 min | curierii experimentați livrează mai eficient       |


4. Relevanța datelor generate pentru problemă

Datele sintetice sunt importante pentru:

A. Creșterea volumului datasetului

Ajută la prevenirea overfitting-ului modelului de rețea neuronală.

B. Captarea variabilității reale

Simularea introduce variații naturale din scenarii precum:

-trafic intens
-condiții meteo nefavorabile
-diferențe între vehicule
-experiență curieri

C. Continuitate între date reale și simulate

Formatul, tipurile variabilelor și distribuțiile sunt compatibile cu datasetul real disponibil.

D. Relevanță pentru logistică

Toți parametrii simulați sunt folosiți în practică de aplicații reale precum Glovo, Tazz, Bolt Food.

5. Fișiere generate

Modulul produce următoarele fișiere:

data/generated/generated_deliveries.csv
docs/generated_vs_real.png
docs/hist_delivery_time_compare.png
docs/boxplot_delivery_time_compare.png
docs/scatter_distance_delivery_compare.png
docs/scatter_prep_vs_delivery_compare.png
docs/scatter_experience_vs_delivery_compare.png
docs/data_statistics.csv

Acestea oferă dovezi vizuale și statistice că datele generate sunt coerente cu datele reale.

6. Concluzie

Modulul de generare a datelor este complet funcțional și produce date sintetice realiste, consistente cu datele reale și esențiale pentru îmbogățirea datasetului final folosit la antrenarea rețelei neuronale.