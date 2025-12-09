Dataset Description – Food Delivery Times (Real Data)

1. Sursa datasetului

Nume dataset: Food Delivery Time Prediction

Proveniență: Kaggle

Link sursă:
https://www.kaggle.com/datasets/denkuznetz/food-delivery-time-prediction

Număr de observații: 1000 rânduri

Format: CSV

Datasetul conține informații despre timpi reali de livrare pentru comenzi alimentare, incluzând factori care influențează durata finală a livrării.

2. Caracteristicile datasetului

| Coloana                    | Tip              | Descriere                            | Exemplu            |
| -------------------------- | ---------------- | ------------------------------------ | ------------------ |
| **Distance_km**            | numeric          | Distanța dintre restaurant și client | 7.93               |
| **Weather**                | categorial       | Condiții meteo                       | Clear, Rainy       |
| **Traffic_Level**          | categorial       | Nivelul traficului                   | Low, Medium, High  |
| **Time_of_Day**            | categorial       | Momentul zilei                       | Morning, Afternoon |
| **Vehicle_Type**           | categorial       | Tipul vehiculului curierului         | Bike, Scooter, Car |
| **Preparation_Time_min**   | numeric          | Durata pregătirii comenzii           | 12                 |
| **Courier_Experience_yrs** | numeric          | Experiența curierului (ani)          | 1                  |
| **Delivery_Time_min**      | numeric (target) | Timpul real de livrare               | 43                 |


3. Scopul datasetului

Acest dataset este utilizat pentru construirea unui model de Rețea Neurală capabil să prezică timpul de livrare al comenzilor de mâncare pe baza caracteristicilor operaționale (trafic, vehicul, distanță, meteo etc.).

4. Probleme identificate în analiza inițială (EDA)

distribuție neuniformă în Traffic_Level (mai multe cazuri “Low”)

variații mari în Delivery_Time_min

valori lipsă în unele înregistrări (curățate ulterior)

5. Structura finală a datelor după preprocesare

Train: 70%

Validation: 15%

Test: 15%

Date scalate numeric + encoded categorical.