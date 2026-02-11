# 📘 README – Etapa 5: Configurarea și Antrenarea Modelului RN

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** [Belu Maria Alexandra]  
**Link Repository GitHub:** [ https://github.com/belualexandra/Retele-Neuronale.git ]  
**Data predării:** [13.01.2026]

---

## Scopul Etapei 5

Această etapă corespunde punctului **6. Configurarea și antrenarea modelului RN** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.

**Obiectiv principal:** Antrenarea efectivă a modelului RN definit în Etapa 4, evaluarea performanței și integrarea în aplicația completă.

**Pornire obligatorie:** Arhitectura completă și funcțională din Etapa 4:
- State Machine definit și justificat
- Cele 3 module funcționale (Data Logging, RN, UI)
- Minimum 40% date originale în dataset

---

## PREREQUISITE – Verificare Etapa 4 (OBLIGATORIU)

**Înainte de a începe Etapa 5, verificați că aveți din Etapa 4:**

- [X] **State Machine** definit și documentat în `docs/state_machine.*`
- [X] **Contribuție ≥40% date originale** în `data/generated/` (verificabil)
- [X] **Modul 1 (Data Logging)** funcțional - produce CSV-uri
- [X] **Modul 2 (RN)** cu arhitectură definită dar NEANTRENATĂ (`models/untrained_model.h5`)
- [X] **Modul 3 (UI/Web Service)** funcțional cu model dummy
- [X] **Tabelul "Nevoie → Soluție → Modul"** complet în README Etapa 4

** Dacă oricare din punctele de mai sus lipsește → reveniți la Etapa 4 înainte de a continua.**

---

## Pregătire Date pentru Antrenare 

### Dacă ați adăugat date noi în Etapa 4 (contribuția de 40%):

**TREBUIE să refaceți preprocesarea pe dataset-ul COMBINAT:**

Exemplu:
```bash
# 1. Combinare date vechi (Etapa 3) + noi (Etapa 4)
python src/preprocessing/combine_datasets.py

# 2. Refacere preprocesare COMPLETĂ
python src/preprocessing/data_cleaner.py
python src/preprocessing/feature_engineering.py
python src/preprocessing/data_splitter.py --stratify --random_state 42

# Verificare finală:
# data/train/ → trebuie să conțină date vechi + noi
# data/validation/ → trebuie să conțină date vechi + noi
# data/test/ → trebuie să conțină date vechi + noi
```

** ATENȚIE - Folosiți ACEIAȘI parametri de preprocesare:**
- Același `scaler` salvat în `config/preprocessing_params.pkl`
- Aceiași proporții split: 70% train / 15% validation / 15% test
- Același `random_state=42` pentru reproducibilitate

**Verificare rapidă:**
```python
import pandas as pd
train = pd.read_csv('data/train/X_train.csv')
print(f"Train samples: {len(train)}")  # Trebuie să includă date noi
```

---

##  Cerințe Structurate pe 3 Niveluri

### Nivel 1 – Obligatoriu pentru Toți (70% din punctaj)

Completați **TOATE** punctele următoare:

1. **Antrenare model** definit în Etapa 4 pe setul final de date (≥40% originale)
2. **Minimum 10 epoci**, batch size 8–32
3. **Împărțire stratificată** train/validation/test: 70% / 15% / 15%
4. **Tabel justificare hiperparametri** (vezi secțiunea de mai jos - OBLIGATORIU)
5. **Metrici calculate pe test set:**
   - **Acuratețe ≥ 65%**
   - **F1-score (macro) ≥ 0.60**
6. **Salvare model antrenat** în `models/trained_model.h5` (Keras/TensorFlow) sau `.pt` (PyTorch) sau `.lvmodel` (LabVIEW)
7. **Integrare în UI din Etapa 4:**
   - UI trebuie să încarce modelul ANTRENAT (nu dummy)
   - Inferență REALĂ demonstrată
   - Screenshot în `docs/screenshots/inference_real.png`

#### Tabel Hiperparametri și Justificări (OBLIGATORIU - Nivel 1)

Completați tabelul cu hiperparametrii folosiți și **justificați fiecare alegere**:

| **Hiperparametru** | **Valoare Aleasă** | **Justificare** |
|--------------------|-------------------|-----------------|
| Learning rate | Ex: 0.001 | Valoare standard pentru Adam optimizer, asigură convergență stabilă |
| Batch size | Ex: 32 | Compromis memorie/stabilitate pentru N=[numărul vostru] samples |
| Number of epochs | Ex: 50 | Cu early stopping după 10 epoci fără îmbunătățire |
| Optimizer | Ex: Adam | Adaptive learning rate, potrivit pentru RN cu [numărul vostru] straturi |
| Loss function | Ex: Categorical Crossentropy | Clasificare multi-class cu K=[numărul vostru] clase |
| Activation functions | Ex: ReLU (hidden), Softmax (output) | ReLU pentru non-linearitate, Softmax pentru probabilități clase |


| **Hiperparametru**          |                                                        **Valoare Aleasă** | **Justificare**                                                                                                                                                                                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Learning rate               |                                                       **0.001 (inițial)** | Valoare standard pentru **Adam**, oferă convergență stabilă și rapidă pentru un MLP pe date tabulare. În proiect a fost folosit și **ReduceLROnPlateau**, care reduce automat learning rate-ul când performanța pe validare stagnează, ceea ce ajută la fine-tuning și generalizare. |
| Batch size                  |                                                                    **32** | Compromis între stabilitatea gradientului și viteză. Pentru **N_train = 7700** rezultă aproximativ **7700/32 ≈ 241** iterații/epocă, suficient pentru o antrenare stabilă fără consum mare de memorie sau timp.                                                                      |
| Number of epochs            |                                             **max 40** (cu EarlyStopping) | Numărul maxim permite convergență completă, dar antrenarea este controlată prin **EarlyStopping** (monitor pe validare), astfel încât modelul se oprește automat când nu mai există îmbunătățiri, prevenind overfitting-ul.                                                          |
| Optimizer                   |                                                                  **Adam** | Optimizer adaptiv potrivit pentru rețele MLP și date tabulare: ajustează automat rata de învățare pe parametri și converge rapid, fiind mai robust decât SGD simplu în practică.                                                                                                     |
| Loss function (regresie)    |                                              **MSE (Mean Squared Error)** | Pentru predicția timpului de livrare (`Delivery_Time_min`), MSE penalizează mai puternic erorile mari și ajută modelul să evite predicții extreme. Performanța finală este raportată și prin **MAE** (mai intuitiv, în minute).                                                      |
| Loss function (clasificare) |                                       **Sparse Categorical Crossentropy** | Clasificare multi-clasă cu **K = 3 clase** (fast/medium/slow) folosind etichete numerice **0/1/2** (fără one-hot), deci această funcție este alegerea corectă.                                                                                                                       |
| Activation functions        | **ReLU** (hidden), **Linear** (output minute), **Softmax** (output clasă) | ReLU introduce non-linearitate și accelerează antrenarea. Output-ul pentru regresie este **linear** deoarece prezicem o valoare reală (minute). Softmax este standard pentru clasificare multi-clasă și produce probabilități pe cele 3 clase.                                       |
| Callbacks                   |                     **ModelCheckpoint, EarlyStopping, ReduceLROnPlateau** | ModelCheckpoint salvează **best_model** pe baza performanței pe validare. EarlyStopping previne supraînvățarea. ReduceLROnPlateau scade automat LR la stagnare, ajutând modelul să atingă un minim mai bun.                                                                          |
| Metrici monitorizate        |                             **MAE (minute), Accuracy & F1 macro (clase)** | MAE este metrică principală deoarece aplicația trebuie să prezică corect timpul în minute. Accuracy și F1 macro sunt folosite pentru evaluarea echilibrată a clasificării (mai ales când distribuția claselor nu e perfect uniformă).                                                |




**Justificare detaliată batch size (exemplu):**
```

Am ales batch_size = 32 deoarece setul de antrenare conține N_train = 7700 observații,
rezultând aproximativ 7700 / 32 ≈ 241 iterații per epocă.

Această valoare oferă:
- stabilitate a gradientului (batch-uri prea mici → gradient mai zgomotos),
- timp de antrenare rezonabil,
- consum de memorie controlat,
- generalizare bună față de batch-uri foarte mari.


```

**Resurse învățare rapidă:**
- Împărțire date: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html (video 3 min: https://youtu.be/1NjLMWSGosI?si=KL8Qv2SJ1d_mFZfr)  
- Antrenare simplă Keras: https://keras.io/examples/vision/mnist_convnet/ (secțiunea „Training”)  
- Antrenare simplă PyTorch: https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#training-an-image-classifier (video 2 min: https://youtu.be/ORMx45xqWkA?si=FXyQEhh0DU8VnuVJ)  
- F1-score: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html (video 4 min: https://youtu.be/ZQlEcyNV6wc?si=VMCl8aGfhCfp5Egi)


---

### Nivel 2 – Recomandat (85-90% din punctaj)

Includeți **TOATE** cerințele Nivel 1 + următoarele:

1. **Early Stopping** - oprirea antrenării dacă `val_loss` nu scade în 5 epoci consecutive
2. **Learning Rate Scheduler** - `ReduceLROnPlateau` sau `StepLR`
3. **Augmentări relevante domeniu:**
   - Vibrații motor: zgomot gaussian calibrat, jitter temporal
   - Imagini industriale: slight perspective, lighting variation (nu rotații simple!)
   - Serii temporale: time warping, magnitude warping
4. **Grafic loss și val_loss** în funcție de epoci salvat în `docs/loss_curve.png`
5. **Analiză erori context industrial** (vezi secțiunea dedicată mai jos - OBLIGATORIU Nivel 2)

**Indicatori țintă Nivel 2:**
- **Acuratețe ≥ 75%**
- **F1-score (macro) ≥ 0.70**

TEST MAE (minutes): 2.883
TEST RMSE (minutes): 4.277
TEST Accuracy (class): 0.825
TEST F1 macro (class): 0.793


**Resurse învățare (aplicații industriale):**
- Albumentations: https://albumentations.ai/docs/examples/   
- Early Stopping + ReduceLROnPlateau în Keras: https://keras.io/api/callbacks/   
- Scheduler în PyTorch: https://pytorch.org/docs/stable/optim.html#how-to-adjust-learning-rate 

---

### Nivel 3 – Bonus (până la 100%)

**Punctaj bonus per activitate:**

| **Activitate** |  **Livrabil** |
|----------------|--------------|
| Comparare 2+ arhitecturi diferite | Tabel comparativ + justificare alegere finală în README |
| Export ONNX/TFLite + benchmark latență | Fișier `models/final_model.onnx` + demonstrație <50ms |
| Confusion Matrix + analiză 5 exemple greșite | `docs/confusion_matrix.png` + analiză în README |

am comparat arhitectura de bază (Baseline) cu varianta optimizată pentru a valida eficiența tehnicilor de regularizare și a noii structuri a rețelei

| Metrică | Arhitectura Baseline (Etapa 5) | Arhitectura Optimizată (Etapa 6) | Progres / Impact |
| :--- | :--- | :--- | :--- |
| **Configurație Straturi** | `[64, 32]` neuroni | `[128, 64]` neuroni | **+ Capacitate** (model mai complex) |
| **Tehnici Regularizare** | N/A | Dropout + Batch Normalization | **+ Stabilitate** (previne overfitting) |
| **Acuratețe Clasificare** | 83.57% | **88.00%** | **+4.43%** (îmbunătățire semnificativă) |
| **Eroare Timp (MAE)** | 2.95 min | **2.93 min** | **-0.02 min** (precizie ușor crescută) |
| **Learning Rate Final** | 3.12e-05 | 1.00e-05 | **Convergență fină** |


Am selectat Arhitectura Optimizată (Etapa 6) ca model final pentru implementare din următoarele motive:

Modelul a atins o acuratețe de 88.00% pe datele de validare, depășind pragul de 83.57% al modelului baseline. Această îmbunătățire se datorează stratului mai dens de 128 de neuroni care capturează mai bine interacțiunile non-liniare dintre factorii de trafic și distanță.

Introducerea straturilor de Dropout (0.25) a permis modelului să evite overfitting-ul (suprainvățarea), menținând o performanță constantă pe setul de test, în ciuda creșterii complexității rețelei.

Eroarea medie absolută (MAE) a fost menținută sub pragul de 3 minute (2.93 min), asigurând o estimare a timpului de livrare extrem de utilă pentru utilizatorul final.


**Resurse bonus:**
- Export ONNX din PyTorch: [PyTorch ONNX Tutorial](https://pytorch.org/tutorials/beginner/onnx/export_simple_model_to_onnx_tutorial.html)
- TensorFlow Lite converter: [TFLite Conversion Guide](https://www.tensorflow.org/lite/convert)
- Confusion Matrix analiză: [Scikit-learn Confusion Matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)

---

## Verificare Consistență cu State Machine (Etapa 4)

Antrenarea și inferența trebuie să respecte fluxul din State Machine-ul vostru definit în Etapa 4.

**Exemplu pentru monitorizare vibrații lagăr:**

| **Stare din Etapa 4** | **Implementare în Etapa 5** |
|-----------------------|-----------------------------|
| `ACQUIRE_DATA` | Citire batch date din `data/train/` pentru antrenare |
| `PREPROCESS` | Aplicare scaler salvat din `config/preprocessing_params.pkl` |
| `RN_INFERENCE` | Forward pass cu model ANTRENAT (nu weights random) |
| `THRESHOLD_CHECK` | Clasificare Normal/Uzură pe baza output RN antrenat |
| `ALERT` | Trigger în UI bazat pe predicție modelului real |

**În `src/app/main.py` (UI actualizat):**

Verificați că **TOATE stările** din State Machine sunt implementate cu modelul antrenat:

```python
# ÎNAINTE (Etapa 4 - model dummy):
model = keras.models.load_model('models/untrained_model.h5')  # weights random
prediction = model.predict(input_scaled)  # output aproape aleator

# ACUM (Etapa 5 - model antrenat):
model = keras.models.load_model('models/trained_model.h5')  # weights antrenate
prediction = model.predict(input_scaled)  # predicție REALĂ și corectă
```

---

## Analiză Erori în Context Industrial (OBLIGATORIU Nivel 2)

**Nu e suficient să raportați doar acuratețea globală.** Analizați performanța în contextul aplicației voastre industriale:

### 1. Pe ce clase greșește cel mai mult modelul?


**Completați pentru proiectul vostru:**
```

1. Pe ce clase greșește cel mai mult modelul?

Analiza erorilor pe baza matricei de confuzie arată că modelul realizează cele mai frecvente confuzii între clasele „medium” și „slow”, respectiv într-o măsură mai mică între „fast” și „medium”. Confuziile între clasele extreme („fast” ↔ „slow”) sunt rare, ceea ce indică faptul că modelul reușește să distingă corect scenariile clar diferite de livrare.

Cauze posibile ale acestor confuzii

Principalele cauze ale erorilor identificate sunt:

Suprapunerea naturală a caracteristicilor între clasele „medium” și „slow”. De exemplu, comenzile cu distanță medie (8–12 km), trafic moderat și vreme nefavorabilă pot avea timpi de livrare aflați la limita dintre cele două clase.

Definirea claselor pe praguri de timp, unde mici variații (zgomot, condiții meteo sau trafic) pot muta o comandă de la o clasă la alta, deși scenariul operațional este foarte similar.

Informație incompletă despre contextul real, deoarece modelul nu dispune de date precum întârzieri neprevăzute (accidente, lucrări rutiere), care în practică pot influența livrarea și pot duce la etichete ambigue.

Interpretare în context industrial

În contextul unei aplicații reale de livrare de mâncare, aceste erori sunt acceptabile din punct de vedere operațional, deoarece:

confuziile apar între clase adiacente („medium” vs „slow”), nu între extreme;

impactul asupra clientului final este redus (diferența de câteva minute între „medium” și „slow”);

predicția numerică a timpului (regresie) rămâne precisă, cu un MAE de aproximativ 2.9 minute, ceea ce permite sistemului să ofere o estimare realistă chiar și atunci când clasa este ușor greșită.

Concluzie

Modelul greșește predominant în zonele de graniță dintre clase, unde scenariile sunt dificil de separat chiar și pentru un operator uman. Acest comportament este tipic și acceptabil pentru sisteme SIA utilizate în aplicații industriale, demonstrând o bună capacitate de generalizare și o înțelegere corectă a relațiilor dintre variabilele de intrare.

```

### 2. Ce caracteristici ale datelor cauzează erori?



**Completați pentru proiectul vostru:**
```

Analiza performanței modelului în raport cu caracteristicile de intrare indică faptul că erorile apar în principal în scenarii de frontieră, unde valorile feature-urilor sunt intermediare sau contradictorii. Cele mai relevante situații sunt următoarele:

2.1 Distanță medie combinată cu trafic variabil

Modelul are performanță mai slabă pentru comenzile cu distanțe medii (aprox. 8–12 km) atunci când nivelul de trafic și condițiile meteo variază. În aceste cazuri, comenzile pot fi încadrate atât în clasa medium, cât și slow, deoarece mici variații de trafic sau vreme pot influența semnificativ timpul final de livrare.

Cauză:
Distanțele medii nu determină singure clasa de livrare, iar efectul lor este amplificat sau redus de trafic și vreme, ceea ce duce la suprapuneri între clase.

2.2 Experiență medie a curierului

Erori apar mai frecvent pentru curieri cu experiență intermediară (3–6 ani). Spre deosebire de curierii foarte noi sau foarte experimentați, această categorie prezintă o variabilitate mai mare în performanță.

Cauză:
Experiența medie nu garantează un comportament constant; în practică, diferențele individuale dintre curieri nu sunt complet capturate de acest feature numeric.

2.3 Scenarii cu efecte contradictorii între feature-uri

Modelul întâmpină dificultăți atunci când feature-urile transmit semnale opuse, de exemplu:

distanță mică + trafic foarte aglomerat,

distanță mare + trafic scăzut + curier experimentat.

Cauză:
În astfel de cazuri, relațiile dintre variabile sunt puternic neliniare, iar mici variații pot schimba atât timpul estimat, cât și clasa de livrare.

2.4 Zonele de tranziție dintre clase

Cele mai multe erori apar pentru comenzile al căror timp real de livrare este aproape de pragurile de separare dintre clase (ex. limita dintre medium și slow).

Cauză:
Etichetarea pe clase se bazează pe praguri fixe de timp, iar zgomotul natural din date (trafic, vreme, întârzieri minore) face ca aceste cazuri să fie dificil de separat chiar și pentru un operator uman.

Concluzie

Modelul are performanță mai slabă în scenarii ambigue, caracterizate prin:

valori intermediare ale distanței,

experiență medie a curierului,

combinații contradictorii de trafic, vreme și moment al zilei,

observații aflate la limita dintre clase.

Aceste limitări sunt inerente problemei și reflectă complexitatea procesului real de livrare, nu o deficiență majoră a arhitecturii sau a procesului de antrenare.

```

### 3. Ce implicații are pentru aplicația industrială?



**Completați pentru proiectul vostru:**
```
În aplicația reală (platformă de livrare mâncare), erorile de clasificare au impact diferit în funcție de tipul lor. În special, ne interesează predicția clasei (fast/medium/slow) deoarece aceasta poate influența decizii operaționale: alocare curieri, estimarea ETA pentru client și prioritizarea comenzilor.

Tipuri de erori și impact

A) FALSE NEGATIVE pentru livrare lentă (Slow prezis ca Medium/Fast) – mai critic

Impact: clientul primește o estimare prea optimistă → scade încrederea în aplicație, apar plângeri, anulări, penalizări (SLA).

În practică: comanda poate fi încadrată ca “normală” și nu primește tratament prioritar (ex. curier mai bun, rută optimizată), deși ar avea nevoie.

B) FALSE POSITIVE pentru livrare lentă (Medium/Fast prezis ca Slow) – mai acceptabil

Impact: clientul primește o estimare conservatoare (mai mare) → de obicei e mai tolerabil decât întârzierea neanunțată.

În practică: pot fi alocate resurse extra (curier mai bun) unor comenzi care nu erau chiar lente → cost operațional ușor mai mare, dar risc scăzut.

C) Confuzie Fast ↔ Medium – impact moderat

Impact: diferența tipică între fast și medium este relativ mică (câteva minute), deci impactul este redus, mai ales dacă predicția de minute (regresie) rămâne precisă.

Observație importantă din matricea de confuzie:
Modelul face foarte rar confuzii între clasele extreme (Fast ↔ Slow), ceea ce este foarte bine pentru aplicație: nu “promite” livrare rapidă când de fapt este foarte lentă.

Prioritate în context industrial

Prioritatea principală: minimizarea situațiilor în care o livrare cu adevărat lentă este prezisă ca fiind mai rapidă (Slow → Medium/Fast).
Chiar dacă asta crește ușor alarmele false (Medium → Slow), este preferabil operațional.

Măsură practică de reducere a riscului (fără retraining)

În aplicația web putem adopta o regulă de decizie mai conservatoare pentru clasa Slow:

în loc să alegem strict clasa cu probabilitatea maximă,

marcăm comanda ca Slow dacă P(Slow) depășește un prag mai mic decât 0.5.

Exemplu de politică:

dacă P(Slow) ≥ 0.35 → considerăm comanda “Slow” (prioritizare, ETA mai conservator)

altfel → luăm argmax (Fast/Medium)

Această ajustare reduce riscul de subestimare a întârzierilor, chiar dacă poate crește ușor numărul de comenzi etichetate “Slow” (cost operațional minor, dar satisfacție client mai bună).

Concluzie

În contextul aplicației industriale de livrare, erorile de tip “subestimare” (Slow prezis ca Medium/Fast) sunt cele mai problematice, deoarece afectează direct experiența clientului și respectarea SLA.
Prin urmare, sistemul trebuie să fie ușor conservator în detectarea comenzilor lente, chiar cu prețul unor false positives. Predicția numerică a timpului (MAE mic) rămâne utilă pentru a comunica ETA realist, iar clasificarea este folosită ca suport pentru decizii operaționale.


```

### 4. Ce măsuri corective propuneți?

**Completați pentru proiectul vostru:**
```


Măsuri corective (propuneri concrete):

1. Colectare / generare suplimentară de date pentru cazurile de graniță (Medium–Slow)

Țintă: comenzi cu timp real aproape de pragul dintre medium și slow (ex. ±5 minute față de prag).

Motiv: matricea de confuzie arată că cele mai multe erori sunt între Medium ↔ Slow, deci acolo modelul are nevoie de mai multe exemple.

Implementare: în generator, creștem proporția de scenarii cu distanțe medii (8–12 km), trafic mediu–ridicat și vreme variabilă, astfel încât modelul să vadă mai multe situații „ambigue”.

2. Cost sensibil la risc: penalizare mai mare pentru erorile Slow → Medium (subestimare)

În aplicația reală, subestimarea timpului (a prezice prea optimist) este mai gravă decât supraestimarea.

Soluție: folosim o funcție de loss ponderată sau sample weights pe ieșirea de clasificare, astfel încât erorile în care „Slow este prezis ca Medium/Fast” să fie mai penalizate.

Alternativ (fără retraining): setăm un prag conservator în inferență: dacă P(Slow) ≥ 0.35, marcăm comanda ca Slow.

3. Adăugare de feature-uri operaționale care lipsesc și reduc ambiguitatea

Datele actuale nu surprind anumiți factori reali care provoacă întârzieri:

„Restaurant load” (cât de aglomerat e restaurantul)

„Courier current workload” (câte comenzi are curierul deja)

„Zone/City” sau densitatea zonei (urban vs periferie)

Beneficiu: reduce cazurile în care aceeași combinație (distanță + trafic + vreme) poate avea timpi diferiți în realitate.

4. Calibrare / post-procesare pentru predicția în minute (constrângeri realiste)

Introducem reguli de siguranță pentru ETA:

limitare intervale (ex. 10–180 minute)

„smoothing” pentru valori extreme

folosirea clasei prezise ca factor de ajustare mic (ex. dacă e Slow, +2–5 minute) ca să evităm subestimarea.

Beneficiu: predicții mai stabile și mai credibile în aplicația web.

5. Validare suplimentară pe „scenarii rare” și monitorizare în producție

Creăm un set de test „stress” (ex.: vreme rea + trafic ridicat + distanță mare) și verificăm performanța separat.

În aplicație, logăm predicțiile și eroarea reală (când avem feedback) pentru a detecta degradarea modelului în timp (data drift).


```

---

## Structura Repository-ului la Finalul Etapei 5

**Clarificare organizare:** Vom folosi **README-uri separate** pentru fiecare etapă în folderul `docs/`:

```
proiect-rn-[prenume-nume]/
├── README.md                           # Overview general proiect (actualizat)
├── etapa3_analiza_date.md         # Din Etapa 3
├── etapa4_arhitectura_sia.md      # Din Etapa 4
├── etapa5_antrenare_model.md      # ← ACEST FIȘIER (completat)
│
├── docs/
│   ├── state_machine.png              # Din Etapa 4
│   ├── loss_curve.png                 # NOU - Grafic antrenare
│   ├── confusion_matrix.png           # (opțional - Nivel 3)
│   └── screenshots/
│       ├── inference_real.png         # NOU - OBLIGATORIU
│       └── ui_demo.png                # Din Etapa 4
│
├── data/                               # Din Etapa 3-4 (NESCHIMBAT)
│   ├── raw/
│   ├── generated/                     # Contribuția voastră 40%
│   ├── processed/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── src/
│   ├── data_acquisition/              # Din Etapa 4
│   ├── preprocessing/                 # Din Etapa 3
│   │   └── combine_datasets.py        # NOU (dacă ați adăugat date în Etapa 4)
│   ├── neural_network/
│   │   ├── model.py                   # Din Etapa 4
│   │   ├── train.py                   # NOU - Script antrenare
│   │   └── evaluate.py                # NOU - Script evaluare
│   └── app/
│       └── main.py                    # ACTUALIZAT - încarcă model antrenat
│
├── models/
│   ├── untrained_model.h5             # Din Etapa 4
│   ├── trained_model.h5               # NOU - OBLIGATORIU
│   └── final_model.onnx               # (opțional - Nivel 3 bonus)
│
├── results/                            # NOU - Folder rezultate antrenare
│   ├── training_history.csv           # OBLIGATORIU - toate epoch-urile
│   ├── test_metrics.json              # Metrici finale pe test set
│   └── hyperparameters.yaml           # Hiperparametri folosiți
│
├── config/
│   └── preprocessing_params.pkl       # Din Etapa 3 (NESCHIMBAT)
│
├── requirements.txt                    # Actualizat
└── .gitignore
```

**Diferențe față de Etapa 4:**
- Adăugat `docs/etapa5_antrenare_model.md` (acest fișier)
- Adăugat `docs/loss_curve.png` (Nivel 2)
- Adăugat `models/trained_model.h5` - OBLIGATORIU
- Adăugat `results/` cu history și metrici
- Adăugat `src/neural_network/train.py` și `evaluate.py`
- Actualizat `src/app/main.py` să încarce model antrenat

---

## Instrucțiuni de Rulare (Actualizate față de Etapa 4)

### 1. Setup mediu (dacă nu ați făcut deja)

```bash
pip install -r requirements.txt
```

### 2. Pregătire date (DACĂ ați adăugat date noi în Etapa 4)

```bash
# Combinare + reprocesare dataset complet
python src/preprocessing/combine_datasets.py
python src/preprocessing/data_cleaner.py
python src/preprocessing/feature_engineering.py
python src/preprocessing/data_splitter.py --stratify --random_state 42
```

### 3. Antrenare model

```bash
python src/neural_network/train.py --epochs 50 --batch_size 32 --early_stopping

# Output așteptat:
# Epoch 1/50 - loss: 0.8234 - accuracy: 0.6521 - val_loss: 0.7891 - val_accuracy: 0.6823
# ...
# Epoch 23/50 - loss: 0.3456 - accuracy: 0.8234 - val_loss: 0.4123 - val_accuracy: 0.7956
# Early stopping triggered at epoch 23
# ✓ Model saved to models/trained_model.h5
```

### 4. Evaluare pe test set

```bash
python src/neural_network/evaluate.py --model models/trained_model.h5

# Output așteptat:
# Test Accuracy: 0.7823
# Test F1-score (macro): 0.7456
# ✓ Metrics saved to results/test_metrics.json
# ✓ Confusion matrix saved to docs/confusion_matrix.png
```

### 5. Lansare UI cu model antrenat

```bash
streamlit run src/app/main.py

# SAU pentru LabVIEW:
# Deschideți WebVI și rulați main.vi
```

**Testare în UI:**
1. Introduceți date de test (manual sau upload fișier)
2. Verificați că predicția este DIFERITĂ de Etapa 4 (când era random)
3. Verificați că confidence scores au sens (ex: 85% pentru clasa corectă)
4. Faceți screenshot → salvați în `docs/screenshots/inference_real.png`

---

## Checklist Final – Bifați Totul Înainte de Predare

### Prerequisite Etapa 4 (verificare)
- [X] State Machine există și e documentat în `docs/state_machine.*`
- [X] Contribuție ≥40% date originale verificabilă în `data/generated/`
- [X] Cele 3 module din Etapa 4 funcționale

### Preprocesare și Date
- [X] Dataset combinat (vechi + nou) preprocesat (dacă ați adăugat date)
- [X] Split train/val/test: 70/15/15% (verificat dimensiuni fișiere)
- [X] Scaler din Etapa 3 folosit consistent (`config/preprocessing_params.pkl`)

### Antrenare Model - Nivel 1 (OBLIGATORIU)
- [X] Model antrenat de la ZERO (nu fine-tuning pe model pre-antrenat)
- [X] Minimum 10 epoci rulate (verificabil în `results/training_history.csv`)
- [X] Tabel hiperparametri + justificări completat în acest README
- [X] Metrici calculate pe test set: **Accuracy ≥65%**, **F1 ≥0.60**
- [X] Model salvat în `models/trained_model.h5` (sau .pt, .lvmodel)
- [X] `results/training_history.csv` există cu toate epoch-urile

### Integrare UI și Demonstrație - Nivel 1 (OBLIGATORIU)
- [X] Model ANTRENAT încărcat în UI din Etapa 4 (nu model dummy)
- [X] UI face inferență REALĂ cu predicții corecte
- [X] Screenshot inferență reală în `docs/screenshots/inference_real.png`
- [X] Verificat: predicțiile sunt diferite față de Etapa 4 (când erau random)

### Documentație Nivel 2 (dacă aplicabil)
- [X] Early stopping implementat și documentat în cod
- [X] Learning rate scheduler folosit (ReduceLROnPlateau / StepLR)
- [X] Augmentări relevante domeniu aplicate (NU rotații simple!)
- [X] Grafic loss/val_loss salvat în `docs/loss_curve.png`
- [X] Analiză erori în context industrial completată (4 întrebări răspunse)
- [X] Metrici Nivel 2: **Accuracy ≥75%**, **F1 ≥0.70**

### Documentație Nivel 3 Bonus (dacă aplicabil)
- [X] Comparație 2+ arhitecturi (tabel comparativ + justificare) 
- [X] Export ONNX/TFLite + benchmark latență (<50ms demonstrat)
- [X] Confusion matrix + analiză 5 exemple greșite cu implicații  

### Verificări Tehnice
- [X] `requirements.txt` actualizat cu toate bibliotecile noi
- [X] Toate path-urile RELATIVE (nu absolute: `/Users/...` )
- [X] Cod nou comentat în limba română sau engleză (minimum 15%)
- [X] `git log` arată commit-uri incrementale (NU 1 commit gigantic)
- [X] Verificare anti-plagiat: toate punctele 1-5 respectate

### Verificare State Machine (Etapa 4)
- [X] Fluxul de inferență respectă stările din State Machine
- [X] Toate stările critice (PREPROCESS, INFERENCE, ALERT) folosesc model antrenat
- [X] UI reflectă State Machine-ul pentru utilizatorul final

### Pre-Predare
- [X] `docs/etapa5_antrenare_model.md` completat cu TOATE secțiunile
- [X] Structură repository conformă: `docs/`, `results/`, `models/` actualizate
- [X] Commit: `"Etapa 5 completă – Accuracy=X.XX, F1=X.XX"`
- [X] Tag: `git tag -a v0.5-model-trained -m "Etapa 5 - Model antrenat"`
- [X] Push: `git push origin main --tags`
- [X] Repository accesibil (public sau privat cu acces profesori)

---

## Livrabile Obligatorii (Nivel 1)

Asigurați-vă că următoarele fișiere există și sunt completate:

1. **`docs/etapa5_antrenare_model.md`** (acest fișier) cu:
   - Tabel hiperparametri + justificări (complet)
   - Metrici test set raportate (accuracy, F1)
   - (Nivel 2) Analiză erori context industrial (4 paragrafe)

2. **`models/trained_model.h5`** (sau `.pt`, `.lvmodel`) - model antrenat funcțional

3. **`results/training_history.csv`** - toate epoch-urile salvate

4. **`results/test_metrics.json`** - metrici finale:

Exemplu:
```json
{
  "test_accuracy": 0.7823,
  "test_f1_macro": 0.7456,
  "test_precision_macro": 0.7612,
  "test_recall_macro": 0.7321
}
```

5. **`docs/screenshots/inference_real.png`** - demonstrație UI cu model antrenat

6. **(Nivel 2)** `docs/loss_curve.png` - grafic loss vs val_loss

7. **(Nivel 3)** `docs/confusion_matrix.png` + analiză în README

---

## Predare și Contact

**Predarea se face prin:**
1. Commit pe GitHub: `"Etapa 5 completă – Accuracy=X.XX, F1=X.XX"`
2. Tag: `git tag -a v0.5-model-trained -m "Etapa 5 - Model antrenat"`
3. Push: `git push origin main --tags`

---

**Mult succes! Această etapă demonstrează că Sistemul vostru cu Inteligență Artificială (SIA) funcționează în condiții reale!**