## 1. Metoda de Generare / Achiziție Explicată
Pentru a asigura volumul necesar antrenării rețelelor neuronale și pentru a îndeplini cerința de minimum 40% contribuție originală, am dezvoltat un modul de generare a datelor sintetice bazat pe Simulare Statistică Parametrică.

Metoda nu este o simplă duplicare a datelor existente, ci o reconstrucție a procesului fizic de livrare, folosind următoarea logică:

### I. Generarea Variabilelor Independente (Features)
În loc să folosim o distribuție uniformă simplă (care ar fi nerealistă) sau să copiem distribuția reală, am folosit o abordare hibridă:

Eșantionare Stratificată (Binning) pentru Variabile Critice:

Pentru Distance_km și Courier_Experience_yrs, am definit intervale (bins) specifice.

În interiorul fiecărui interval, am generat valori uniform distribuite.

Scop: Aceasta asigură că modelul vede suficiente exemple și pentru "cazurile rare" (cozi de distribuție), cum ar fi distanțe foarte mari (16-20 km) sau curieri foarte noi (<1 an), care sunt adesea sub-reprezentate în seturile de date reale.

Eșantionare Bazată pe PMF pentru Variabile Categorice:

Pentru Weather, Traffic_Level, Time_of_Day și Vehicle_Type, am calculat distribuția de probabilitate (Probability Mass Function) din setul de date public.

Noile date respectă aceste proporții (de exemplu, dacă 10% din datele reale sunt "Snowy", aproximativ 10% din cele generate vor fi "Snowy").

### II. Generarea Variabilei Țintă
Timpul de livrare (Delivery_Time_min) nu este ales aleatoriu, ci este calculat pe baza unei formule fizice care simulează realitatea, la care se adaugă zgomot stochastic:$$T_{total} = T_{base} + (D \times V_{factor}) + T_{prep} + P_{traffic} + P_{weather} - B_{exp} + \epsilon$$
Unde:

$T_{base}$: Timp minim de bază

$D$: Distanța (km).

$V_{factor}$: Factor de viteză dependent de vehicul.

$T_{prep}$: Timp de preparare a mâncării.

$P_{traffic}, P_{weather}$: Penalizări de timp pentru trafic și vreme rea.

$B_{exp}$: Bonus de timp (eficiență) pentru curierii experimentați.

$\epsilon$: Zgomot aleator (Gaussian Noise).

## 2. Parametri Folosiți
Scriptul de generare este configurat cu următorii parametri tehnici, calibrați pentru a produce date plauzibile fizic:

| Parametru | Valoare / Detalii | Descriere / Sursă în Cod |
| :--- | :--- | :--- |
| **Volum Date (N_SAMPLES)** | 10.000 observații | `generate.py` (linia 12) |
| **Seed (RANDOM_STATE)** | 42 | Asigură reproductibilitatea generării. |
| **Intervale Distanță (DIST_BINS)** | `[0, 4, 8, 12, 16, 20]` km | Asigură acoperire uniformă pe distanțe lungi. |
| **Zgomot Aleator ($\epsilon$)** | Distribuție Normală ($\mu=0, \sigma=2.5$) | Simulează întârzieri neprevăzute (lift, semafor). |
| **Factor Distanță** | ~2.0 - 3.0 min/km | Variază în funcție de tipul vehiculului. |
| **Penalizare Trafic** | High: +10-25 min<br>Medium: +5-15 min | Adăugat dinamic la timpul total. |
| **Penalizare Vreme** | Snowy: +15 min<br>Rainy: +10 min | Simulează condiții adverse de drum. |
| **Bonus Experiență** | Max -0.8 min/an experiență | Modelează eficiența curierilor seniori. |

## 3. Justificarea Relevanței Datelor
Această metodă de achiziție/generare este critică pentru succesul proiectului din următoarele motive:

Augmentarea Volumului de Date:Setul de date public inițial (1.000 observații) era insuficient pentru antrenarea unei rețele neuronale profunde (Deep Learning), care necesită mii de exemple pentru a evita overfitting-ul. Prin generarea a 10.000 de exemple noi, am crescut dimensiunea dataset-ului de 11 ori, permițând modelului să învețe tipare generalizabile.

Corectarea Dezechilibrelor (Bias Correction):Datele reale tind să fie aglomerate în jurul valorilor medii (ex: majoritatea livrărilor sunt la 3-5 km). Metoda de eșantionare stratificată (bins) forțează modelul să învețe și comportamentul sistemului în condiții extreme (distanțe foarte mari sau foarte mici), crescând robustețea algoritmului.

Simularea Variabilității Reale (Noise Injection):Prin introducerea zgomotului Gaussian ($\sigma=2.5$ min), am evitat crearea unui set de date perfect deterministic. Acest lucru obligă rețeaua neuronală să nu memoreze o formulă simplă, ci să învețe tendința centrală și să gestioneze incertitudinea, exact ca într-un scenariu real de producție.

Consistența Fizică:Deși datele sunt sintetice, ele respectă legile fizice (timpul crește odată cu distanța și traficul). Acest lucru garantează că modelul antrenat pe aceste date va fi logic și valid din punct de vedere operațional.