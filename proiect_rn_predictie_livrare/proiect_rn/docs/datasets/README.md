### Datasets – Descriere și Analiză
1. Prezentare generală

Acest proiect utilizează un set de date combinat, format din:

un dataset public (sursă externă),

un dataset generat artificial (contribuție originală),

cu scopul de a antrena și evalua un sistem inteligent pentru predicția timpului de livrare a comenzilor de mâncare și clasificarea acestora în funcție de rapiditatea livrării (fast / medium / slow).

După combinare și preprocesare, setul final de date este utilizat pentru antrenare, validare și testare, respectând proporțiile 70% / 15% / 15%.

2. Dataset public (sursă externă)
2.1 Sursa

Datasetul public a fost preluat dintr-o sursă online deschisă (Kaggle) și conține date istorice despre livrarea comenzilor de mâncare.

2.2 Descriere

Acest set de date include informații relevante pentru procesul de livrare, precum:

distanța de livrare,

condițiile meteo,

nivelul de trafic,

momentul zilei,

tipul vehiculului,

timpul de preparare,

experiența curierului,

timpul real de livrare (minute).

Datele publice oferă un punct de plecare realist, dar prezintă limitări privind distribuția anumitor caracteristici și numărul de scenarii de graniță (medium/slow).

3. Dataset generat artificial (contribuție originală)
3.1 Motivație

Pentru a respecta cerința de minimum 40% contribuție originală și pentru a îmbunătăți capacitatea de generalizare a modelului, a fost implementat un algoritm propriu de generare a datelor.

3.2 Metodă de generare

Datele artificiale au fost generate prin simularea realistă a procesului de livrare, ținând cont de:

distribuții controlate pentru distanță și experiența curierului,

combinații coerente între trafic, vreme și momentul zilei,

relații neliniare între feature-uri și timpul de livrare,

introducerea unui nivel controlat de zgomot pentru realism.

Algoritmul de generare produce:

fișier CSV (generated_data.csv),

raport JSON (generation_report.json) cu statistici descriptive și distribuții.

3.3 Relevanță

Datele generate artificial:

completează zonele slab reprezentate din datasetul public,

cresc numărul de exemple în zonele de tranziție dintre clase,

reduc riscul de overfitting și îmbunătățesc performanța pe setul de test.

4. Dataset final combinat
4.1 Combinare

Datasetul final este obținut prin combinarea datelor publice cu cele generate artificial, utilizând același set de coloane și aceleași tipuri de date.

4.2 Dimensiune

Total observații: ~11.000

Contribuție originală: >40%

Split:

Train: 70%

Validation: 15%

Test: 15%

5. Structura și caracteristicile datelor
5.1 Feature-uri principale

Distance_km – distanța de livrare

Weather – condiții meteo

Traffic_Level – nivel de trafic

Time_of_Day – momentul zilei

Vehicle_Type – tipul vehiculului

Preparation_Time_min – timp de preparare

Courier_Experience_yrs – experiența curierului

5.2 Variabile țintă

Delivery_Time_min – timp de livrare (regresie)

Delivery_Class – clasă de livrare (fast / medium / slow)

6. Analiză vizuală și diagrame

Pentru analiza și validarea calității datelor au fost generate următoarele artefacte:

Diagrame de distribuție (histograme) pentru fiecare feature numeric

Grafic comparativ între datele publice și cele generate (generated_vs_real.png)

Statistici descriptive salvate în data_statistics.csv

Analiza valorilor lipsă și a outlierilor

Aceste diagrame confirmă că datele generate artificial au distribuții compatibile cu cele reale, fără a introduce anomalii majore.

7. Concluzie

Setul de date final combină realismul datelor publice cu flexibilitatea datelor generate artificial, oferind:

acoperire mai bună a scenariilor dificile,

distribuții mai echilibrate,

bază solidă pentru antrenarea și evaluarea unui sistem inteligent aplicabil în context industrial.