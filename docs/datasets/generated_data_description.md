Description of Generated Synthetic Data (Contribuție personală)

1. Scopul generării datelor

Pentru a respecta cerința proiectului (minimum 40% date originale), am dezvoltat un model fizic-sintetic care simulează timpi de livrare bazându-se pe:

distanță
trafic
condiții meteo
momentul zilei
experiența curierului
tipul vehiculului

Acesta permite extinderea datasetului real și îmbunătățirea generalizării rețelei neuronale.

2. Metoda de generare (model fizic)

Timpul de livrare este modelat ca:

delivery_time =
  base_time(distance * speed_factor) +
  preparation_effect +
  traffic_penalty +
  weather_penalty +
  vehicle_factor +
  experience_bonus

Parametri utilizați:

| Parametru        | Explicație                              | Interval   |
| ---------------- | --------------------------------------- | ---------- |
| speed_factor     | minute/km, reprezintă viteza curierului | 2.0 – 4.0  |
| prep_time        | timp pregătire comenzi                  | 5 – 40 min |
| traffic_penalty  | penalizare pentru trafic                | 0 / 4 / 8  |
| weather_penalty  | penalizare meteo                        | 0 / 5 / 10 |
| experience_bonus | curieri experimentați sunt mai rapizi   | 0 – 5 min  |



Generarea se face cu numpy.random pentru realism și reproducibilitate.

3. Volumul datelor generate

700 înregistrări sintetice

Distribuție asemănătoare cu datele reale (verificat prin grafice comparative)

4. Dovezi incluse:

docs/generated_vs_real.png

docs/data_statistics.csv

grafice suplimentare: boxplot, histograme, scatter plots

