Modul de achiziție / generare a datelor
### 1. Metoda de generare a datelor

Datele utilizate în acest proiect sunt obținute printr-o combinație de:

-date reale (dataset public despre timpii de livrare),
-sintetice generate automat, utilizând un model stocastic controlat.

Generarea datelor sintetice este realizată prin scriptul generate.py, care simulează procesul real de livrare a comenzilor de mâncare, ținând cont de factori relevanți precum:

distanța de livrare,
condițiile meteo,
nivelul de trafic,
momentul zilei,
tipul vehiculului utilizat,
experiența curierului.

Valoarea țintă (Delivery_Time_min) este calculată printr-o formulă deterministă extinsă cu zgomot aleator, pentru a reflecta variabilitatea naturală a proceselor reale.
Datele generate sunt salvate în format CSV și sunt complet compatibile cu setul de date public utilizat și cu pipeline-ul de preprocesare definit în Etapa 3.

### 2. Parametrii utilizați în procesul de generare

Dimensiunea setului de date

Număr de observații generate: 10.000

Scop: creșterea volumului de date pentru antrenarea stabilă a unei rețele neuronale

# Distribuții utilizate

-Distance_km: distribuție log-normală (asimetrie pozitivă), limitată între 0.5 și 20 km

-Preparation_Time_min: distribuție triunghiulară (5–30 min), cu valoare medie dominantă

-Courier_Experience_yrs: distribuție Poisson (λ = 2.2), reflectând predominanța curierilor cu experiență redusă

# Variabile categoriale (probabilități controlate)

-Weather: Clear (58%), Rainy (18%), Foggy (10%), Windy (9%), Snowy (5%)

-Traffic_Level: Low (33%), Medium (47%), High (20%)

-Time_of_Day: Morning (24%), Afternoon (32%), Evening (30%), Night (14%)

-Vehicle_Type: Bike (22%), Scooter (38%), Car (40%)

# Zgomot și variabilitate

-Zgomot gaussian adăugat: N(0, 5)

-Scop: evitarea relațiilor deterministe perfecte și creșterea capacității de generalizare a modelului

# Interacțiuni simulate

-Trafic ridicat × distanță mare → penalizare suplimentară

-Vreme nefavorabilă × bicicletă → creștere timp livrare

-Experiență mare × condiții dificile → reducere timp livrare

### 3. Justificarea relevanței datelor pentru problemă

Problema abordată este predicția timpului de livrare a comenzilor de mâncare, o problemă de regresie (și ulterior clasificare) cu aplicații reale în logistică și servicii de livrare.

Datele generate sunt relevante deoarece:

-reproduc relații cauzale realiste (distanță, trafic, vreme),
-includ variabilitate și incertitudine specifică proceselor reale,
-antrenarea unui model capabil să învețe relații neliniare,
-reduc riscul de overfitting asociat seturilor de date mici,
-asigură o contribuție de peste 40% date originale, conform cerințelor proiectului.

Combinarea datelor reale cu cele sintetice permite obținerea unui set de date suficient de mare și divers pentru antrenarea corectă a unei rețele neuronale și pentru realizarea unor predicții stabile și coerente într-o aplicație web.

### 4. Output

Scriptul generate.py produce următoarele fișiere:

data/generated/generated_data.csv – setul de date sintetice

data/generated/generation_report.json – raport statistic al procesului de generare

### 5. Rulare

Pentru generarea datelor, se execută comanda:

python src/data_acquisition/generate.py