# Dataset: Food Delivery Times

* **Origine:** Dataset public disponibil pe platforma Kaggle, titlul: “Food Delivery Time Prediction”, creat de utilizatorul Den Kuznetz.
* **Link sursă:** https://www.kaggle.com/datasets/denkuznetz/food-delivery-time-prediction
* **Modul de achiziție:** Fișier CSV descărcat manual din Kaggle și importat în proiect.
* **Perioada / condițiile colectării:** Set de date sintetic, generat pe baza unor scenarii realiste din domeniul livrării comenzilor de mâncare, incluzând informații despre distanță, trafic, meteo, vehicul și experiența curierului.

### Caracteristicile dataset-ului

* **Număr total de observații:** 1000
* **Număr de caracteristici (features):** 9-> 8 features + 1 target
* **Tipuri de date:**  Numerice, Categoriale 
* **Format fișiere:** CSV 

### Descrierea fiecărei caracteristici

| **Caracteristică**             | **Tip**    | **Unitate** | **Descriere**                               | **Domeniu valori**                   |
| ------------------------------ | ---------- | ----------- | ------------------------------------------- | ------------------------------------ |
| **Order_ID**                   | categorial | –           | Identificator unic pentru fiecare comandă   | ex: 522, 738, 741                    |
| **Distance_km**                | numeric    | km          | Distanța dintre restaurant și client        | ~1 – 20 km                           |
| **Weather**                    | categorial | –           | Condițiile meteo în momentul livrării       | {Clear, Rainy, Foggy, Snowy, Windy}  |
| **Traffic_Level**              | categorial | –           | Nivelul traficului                          | {Low, Medium, High}                  |
| **Time_of_Day**                | categorial | –           | Momentul zilei                              | {Morning, Afternoon, Evening, Night} |
| **Vehicle_Type**               | categorial | –           | Tipul vehiculului utilizat                  | {Bike, Scooter, Car}                 |
| **Preparation_Time_min**       | numeric    | minute      | Timp de pregătire a comenzii în restaurant  | 5 – 30 min                           |
| **Courier_Experience_yrs**     | numeric    | ani         | Experiența curierului                       | 1 – 10 ani                           |
| **Delivery_Time_min (Target)** | numeric    | minute      | Timpul total de livrare, valoarea de prezis | ~24 – 90 min                         |
