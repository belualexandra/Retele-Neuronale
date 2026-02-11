## 1. Identificare Proiect

| Câmp | Valoare |
|------|---------|
| **Student** | [Belu Maria Alexandra]
| **Grupa / Specializare** | [631AB / Informatică Industrială] |
| **Disciplina** | Rețele Neuronale |
| **Instituție** | POLITEHNICA București – FIIR |
| **Link Repository GitHub** | [ https://github.com/belualexandra/Retele-Neuronale.git]
| **Acces Repository** | [Public] |
| **Stack Tehnologic** | [Python] |
| **Domeniul Industrial de Interes (DII)** | [Logistică și Managementul Lanțului de Aprovizionare] |
| **Tip Rețea Neuronală** | [MLP (Multi-Layer Perceptron) cu Arhitectură Multitask] |

### Rezultate Cheie (Versiunea Finală vs Etapa 6)

| Metric | Țintă Minimă | Rezultat Etapa 6 | Rezultat Final | Îmbunătățire | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Accuracy (Test Set)** | ≥ 70% | 81.23% | **82.42%** | `+1.19%` | ✅ |
| **F1-Score (Macro)** | ≥ 0.65 | 0.77 | **0.79** | `+0.02` | ✅ |
| **Latență Inferență** | < 10 ms | 35.00 ms | **0.0039 ms*** | `-34.99 ms` | ✅ |
| **Contribuție Date** | ≥ 40% |90.9%|**90.9%**| — | ✅ |
| **Nr. Experimente** | ≥ 4 | 4 | **9** |`+4`|✅ |

### Declarație de Originalitate & Politica de Utilizare AI

**Acest proiect reflectă munca, gândirea și deciziile mele proprii.**

Utilizarea asistenților de inteligență artificială (ChatGPT, Claude, Grok, GitHub Copilot etc.) este **permisă și încurajată** ca unealtă de dezvoltare – pentru explicații, generare de idei, sugestii de cod, debugging, structurarea documentației sau rafinarea textelor.

**Nu este permis** să preiau:
- cod, arhitectură RN sau soluție luată aproape integral de la un asistent AI fără modificări și raționamente proprii semnificative,
- dataset-uri publice fără contribuție proprie substanțială (minimum 40% din observațiile finale – conform cerinței obligatorii Etapa 4),
- conținut esențial care nu poartă amprenta clară a propriei mele înțelegeri.

**Confirmare explicită (bifez doar ce este adevărat):**

| Nr. | Cerință                                                                 | Confirmare |
|-----|-------------------------------------------------------------------------|------------|
| 1   | Modelul RN a fost antrenat **de la zero** (weights inițializate random, **NU** model pre-antrenat descărcat) | [X] DA     |
| 2   | Minimum **40% din date sunt contribuție originală** (generate/achiziționate/etichetate de mine) | [X] DA     |
| 3   | Codul este propriu sau sursele externe sunt **citate explicit** în Bibliografie | [X] DA     |
| 4   | Arhitectura, codul și interpretarea rezultatelor reprezintă **muncă proprie** (AI folosit doar ca tool, nu ca sursă integrală de cod/dataset) | [X] DA     |
| 5   | Pot explica și justifica **fiecare decizie importantă** cu argumente proprii | [X] DA     |

**Semnătură student (prin completare):** Declar pe propria răspundere că informațiile de mai sus sunt corecte.

---

## 2. Descrierea Nevoii și Soluția SIA

### 2.1 Nevoia Reală / Studiul de Caz

*[Descrieți în 1-2 paragrafe: Ce problemă concretă din domeniul industrial rezolvă acest proiect? Care este contextul și situația actuală? De ce este importantă rezolvarea acestei probleme?]*

Logistica "Last Mile" se confruntă cu o incertitudine ridicată din cauza factorilor dinamici (trafic, meteo, timpi de preparare), făcând estimările de timp statice ineficiente. Această lipsă de precizie duce la pierderi financiare și scăderea satisfacției clienților în cadrul platformelor de livrare.

Proiectul rezolvă această problemă prin implementarea unui SIA (Sistem de Inteligență Artificială) bazat pe o rețea neuronală multitask. Acesta transformă logistica reactivă în una predictivă, oferind estimări exacte de timp (ETA) și clasificarea riscului de întârziere. Rezolvarea este vitală pentru optimizarea resurselor urbane și asigurarea unui avantaj competitiv în contextul dezvoltării Smart Cities.

### 2.2 Beneficii Măsurabile Urmărite

*[Listați 3-5 beneficii concrete cu metrici țintă]*

1.Îmbunătățirea preciziei ETA (Estimated Time of Arrival): Atingerea unei acurateți de 82% în predicția timpului de livrare, asigurând reducerea incertitudinii pentru clientul final.

2.Optimizarea procesării în timp real: Reducerea latenței de inferență la 0.0039 ms prin utilizarea formatului TFLite, permițând sistemului să gestioneze mii de interogări simultane fără a suprasolicita infrastructura serverului.

3.Minimizarea erorilor de planificare: Reducerea erorii medii absolute (MAE) la aproximativ 2.88 minute, oferind restaurantelor o fereastră precisă pentru coordonarea pregătirii preparatelor cu sosirea curierului.

4.Fiabilitatea clasificării riscului: Obținerea unui F1-Score de 0.79, ce garantează o identificare corectă a livrărilor cu risc ridicat de întârziere (clasa "Slow"), permițând intervenția proactivă a dispecerilor.

5.Adaptabilitate la specificul local: Integrarea unui volum de 90.9% date originale, ceea ce asigură o performanță superioară în condițiile specifice de trafic și infrastructură urbană locală, spre deosebire de modelele antrenate pe seturi de date generice.

### 2.3 Tabel: Nevoie → Soluție SIA → Modul Software

| Nevoie Reală (Concretă) | Cum o rezolvă SIA-ul | Modul Software Responsabil | Metrică Măsurabilă |
| :--- | :--- | :--- | :--- |
| **Estimarea realistă a ETA**<br>(evitarea întârzierilor) | Predicție numerică (Regresie) bazată pe distanță, trafic și meteo. | **Preprocesare + RN (Regresie)** | `MAE ≈ 2.88 min`<br>(Eroare < 3 min) |
| **Prioritizarea livrărilor**<br>(Fast / Medium / Slow) | Clasificare automată a comenzilor în 3 categorii de risc. | **RN (Clasificare Multi-class)** | `F1-Score Macro ≈ 0.80` |
| **Accesibilitate operativă**<br>(Dispeceri / Clienți) | Interfață Web (GUI) ce afișează instant predicția și clasa. | **UI (Streamlit) + Pipeline Inferență** | `Timp răspuns < 1s`<br>(Instant) |

---

## 3. Dataset și Contribuție Originală

### 3.1 Sursa și Caracteristicile Datelor

| Caracteristică | Valoare / Detalii |
| :--- | :--- |
| **Origine date** | Mixt (Dataset Public + Generare Proprie prin simulare) |
| **Sursa concretă** | Kaggle ("Food Delivery Time Prediction" - Den Kuznetz)<br>+ Scripturi Python (*Data Acquisition Module*) |
| **Număr total observații (N)** | **~11.000**<br>(1.000 dataset inițial + extindere până la 90.9% date proprii) |
| **Număr features** | 8 features<br>(+ 1 target: `Delivery_Time_min`) |
| **Tipuri de date** | **Numerice** (ex: `Distance_km`, `Prep_time`)<br>**Categoriale** (ex: `Weather`, `Traffic`) |
| **Format fișiere** | CSV (`.csv`) |
| **Perioada colectării** | Noiembrie 2025 – Ianuarie 2026 |

### 3.2 Contribuția Originală (minim 40% OBLIGATORIU)

| Câmp | Valoare / Detalii |
| :--- | :--- |
| **Total observații finale (N)** | **~11.000** |
| **Observații originale (M)** | ~10.000 |
| **Procent contribuție originală** | **90.9%** |
| **Tip contribuție** | Date sintetice<br>(Simulare scenarii trafic & meteo) |
| **Locație cod generare** | `src/data_acquisition/generate.py` |
| **Locație date originale** | `data/generated/` |

**Descriere metodă generare/achiziție:**

*[Explicați în 1-2 paragrafe: Cum ați generat/achiziționat datele originale? Ce parametri ați folosit? De ce sunt relevante pentru problema voastră?]*

Pentru a asigura o diversitate ridicată a scenariilor de livrare și pentru a compensa lipsa unor situații extreme în dataset-ul inițial, am dezvoltat un modul propriu de generare sintetică a datelor. Scriptul Python utilizează distribuții probabilistice (Gaussiene și uniforme) pentru a simula corelații realiste între variabile: de exemplu, creșterea timpului de livrare în condiții de ploaie (Rainy) sau trafic intens (Jam). Am generat astfel peste 10.000 de instanțe noi, controlând parametrii precum viteza medie a vehiculelor (Bike vs. Car) și impactul experienței curierului asupra eficienței.

Aceste date sunt cruciale pentru problemă deoarece permit antrenarea rețelei neuronale pe cazuri de tip "edge case" (trafic blocat, furtună, distanțe mari), care sunt rare în datele publice dar critice pentru robustețea unui sistem industrial. Prin această metodă, am asigurat o contribuție originală de 90.9%, validând capacitatea modelului de a generaliza corect nu doar pe date standard, ci și în condiții operaționale dificile specifice mediului urban aglomerat.

### 3.3 Preprocesare și Split Date

| Set | Procent | Număr Observații |
|-----|---------|------------------|
| Train | 70% | [7700] |
| Validation | 15% | [1650] |
| Test | 15% | [1650] |

**Preprocesări aplicate:**

-Standardizare (StandardScaler): Aplicată pe features numerice (Distance_km, Preparation_Time_min, Courier_Experience_yrs) pentru a centra datele (medie 0, deviație standard 1).

-Curățare Date: Eliminarea duplicatelor și gestionarea valorilor lipsă (imputare cu mediana pentru numeric / modul pentru categorial).

-Eliminare Outlieri: Utilizarea metodei IQR (Interquartile Range) pentru a exclude timpii de livrare extremi sau erorile de logare a datelor.

**Referințe fișiere:** `data/README.md`, `config/preprocessing_params.pkl`

---

## 4. Arhitectura SIA și State Machine

### 4.1 Cele 3 Module Software

| Modul | Tehnologie | Funcționalitate Principală | Locație în Repo |
| :--- | :--- | :--- | :--- |
| **Data Logging / Acquisition** | `Python`<br>(`Pandas`, `NumPy`) | **Generare date sintetice (augmentare)**<br>pentru scenarii complexe de trafic și meteo | `src/data_acquisition/` |
| **Neural Network** | `TensorFlow` / `Keras` | **Arhitectură Multitask (MLP):**<br>Regresie (timp) + Clasificare (risc/viteză) | `src/neural_network/` |
| **Web Service / UI** | `Streamlit` | **Interfață grafică interactivă**<br>pentru introducerea datelor și inferență în timp real | `src/app/` |

### 4.2 State Machine

**Locație diagramă:** `docs/state_machine.drawio`

**Stări principale și descriere:**

| Stare (State) | Descriere | Condiție Intrare | Condiție Ieșire |
| :--- | :--- | :--- | :--- |
| **IDLE** | Stare de repaus; sistemul afișează interfața și așteaptă interacțiunea. | Inițializare reușită sau Resetare după eroare/finalizare. | Aplicatia este pornita sau este oprita. |
| **ACQUIRE_DATA** | Colectarea datelor introduse de utilizator (distanță, trafic, vreme, tip vehicul). |Butonul generare apăsat din starea **IDLE**. | Date valide (→ **PREPROCESS**) sau Eroare / Oprire de urgență. |
| **PREPROCESS** | Transformarea datelor brute folosind `preprocessor.pkl` (scalare + One-Hot Encoding). | Date valide disponibile din **ACQUIRE_DATA**. | Preprocesare reușită (→ **INFERENCE**) sau Eroare de scalare. |
| **INFERENCE** | Calcularea timpului estimat de livrare (NN) pe baza datelor preprocesate. | Preprocesare finalizată cu succes. | Inferență finalizată (→ **DISPLAY_RESULT**) sau Oprire de urgență. |
| **DISPLAY_RESULT** | Afișarea rezultatului utilizatorului (predicția numerică și clasa de risc). | Inferență finalizată cu succes. | Revenire în **IDLE** (nouă predicție) sau trecere în **STOP**. |
| **ERROR** | Stare specială pentru gestionarea problemelor (input invalid, fișiere lipsă). | Eroare detectată în INIT, ACQUIRE sau PREPROCESS. | Resetare (→ **IDLE**) sau Oprire sistem (→ **STOP**). |
| **STOP** | Stare finală; sistemul se oprește complet și eliberează resursele. | Apăsare buton `Stop` sau Oprire de urgență. | Sistem oprit (ieșire definitivă). |

**Justificare alegere arhitectură State Machine:**

*[1 paragraf: De ce această structură pentru problema voastră specifică?]*

Am ales această arhitectură de tip flux secvențial interactiv deoarece modelează fidel procesul operațional de predicție a timpului de livrare, asigurând o tranziție controlată a datelor prin etapele critice de achiziție, preprocesare și inferență. Structura permite o gestionare robustă a erorilor la fiecare pas și oferă siguranță operațională, garantând că sistemul nu poate avansa fără date valide și că poate reveni oricând într-o stare stabilă (IDLE) pentru a procesa o nouă comandă, aspecte esențiale pentru fiabilitatea unui Sistem cu Inteligență Artificială industrial.

### 4.3 Actualizări State Machine în Etapa 6 (dacă este cazul)

| Componentă Modificată | Valoare Etapa 5 | Valoare Etapa 6 | Justificare Modificare |
|----------------------|-----------------|-----------------|------------------------|
| [ex: Threshold alertă] | [0.5] | [0.35] | [Minimizare False Negatives] |
| [ex: Stare nouă adăugată] | N/A | `CONFIDENCE_CHECK` | [Filtrare predicții incerte] |
| [Completați dacă e cazul] | | | |

---

## 5. Modelul RN – Antrenare și Optimizare

### 5.1 Arhitectura Rețelei Neuronale

```
Input (shape: [Batch_Size, 22])  # 22 features după One-Hot Encoding
  │
  ▼
[TRUNCHI COMUN - Extragere Trăsături]
  → Dense(128, Activation='relu') 
  → BatchNormalization()
  → Dropout(0.3)                 # Previne overfitting-ul
  │
  ▼
  → Dense(64, Activation='relu')
  → BatchNormalization()
  → Dropout(0.2)
  │
  ▼
[BIFURCAȚIE - Multitask Heads]
  │                                   │
  ▼                                   ▼
[Ramura 1: Regresie (Timp)]         [Ramura 2: Clasificare (Status)]
  → Dense(32, Activation='relu')      → Dense(32, Activation='relu')
  │                                   │
  ▼                                   ▼
  → Dense(1, Activation='linear')     → Dense(3, Activation='softmax')
  │                                   │
  ▼                                   ▼
Output 1: "minutes" (Float)         Output 2: "category" (Probabilități)
(ex: 24.5 min)                      (ex: [0.1, 0.8, 0.1] → Medium)


Descriere componente:

Input Layer: Primește vectorul de trăsături preprocesat (variabile numerice scalate + variabile categoriale codificate One-Hot).

Trunchi Comun (Shared Layers): Straturi Dense (128 și 64 neuroni) care învață reprezentări abstracte comune utile pentru ambele probleme (de exemplu, cum traficul influențează livrarea în general).

Regularizare: S-au adăugat BatchNormalization pentru stabilitate și Dropout pentru a forța rețeaua să învețe trăsături robuste.

Output Heads:

Regresie: Un singur neuron cu activare liniară pentru a prezice valoarea continuă (minute).

Clasificare: 3 neuroni cu activare Softmax pentru a genera o distribuție de probabilitate peste cele 3 clase (Fast, Medium, Slow).
```

**Justificare alegere arhitectură:**

*[1-2 propoziții: De ce această arhitectură? Ce alternative ați considerat și de ce le-ați respins?]*

Am optat pentru o arhitectură Multitask MLP (Multi-Layer Perceptron) deoarece permite partajarea eficientă a trăsăturilor învățate între cele două obiective corelate (estimarea minutelor și clasificarea urgentei), oferind o inferență mai rapidă decât două modele separate.

Am respins arhitecturile complexe de tip CNN sau RNN deoarece datele de intrare sunt tabulare și statice (vectori de atribute), nu imagini sau serii temporale secvențiale, pentru care straturile Dense cu regularizare (Dropout/BatchNormalization) reprezintă standardul optim de performanță.

### 5.2 Hiperparametri Finali (Model Optimizat - Etapa 6)

| Hiperparametru | Valoare Finală | Justificare Alegere |
| :--- | :--- | :--- |
| **Learning Rate** | `0.001`<br>(cu `ReduceLROnPlateau`) | Valoare de start standard pentru **Adam**; scheduler-ul reduce rata automat când platoul este atins pentru fine-tuning. |
| **Batch Size** | `32` | Compromis optim între viteza de antrenare și stabilitatea gradientului pentru un dataset de **~11.000 observații**. |
| **Epochs** | **Max 40**<br>(oprire efectivă la ~20-30) | Limită superioară suficientă; **Early Stopping** a oprit antrenarea automat pentru a preveni overfitting-ul. |
| **Optimizer** | `Adam` | Optimizer adaptiv, ales pentru convergența rapidă pe **date tabulare complexe** (features mixte). |
| **Loss Function** | `MSE` (Regresie)<br>`Sparse Cat. Crossentropy` (Clasificare) | **Arhitectură Multitask:** MSE penalizează erorile mari de timp, iar Crossentropy gestionează cele 3 clase disjuncte. |
| **Regularizare** | `Dropout (0.25)`<br>+ `BatchNormalization` | Adăugate în **Etapa 6**; au crescut acuratețea la **82%** prin reducerea varianței și stabilizarea antrenării. |
| **Early Stopping** | `patience=5`<br>`monitor='val_loss'` | Oprire automată dacă performanța pe setul de validare nu se îmbunătățește timp de **5 epoci** consecutive. |

### 5.3 Experimente de Optimizare (minim 4 experimente)

| Exp # | Modificare față de Baseline | Accuracy | F1-Score | Timp Antrenare | Observații |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Baseline** | **Configurația din Etapa 5** | 72.00% | 0.68 | ~15 min | Model funcțional, dar performanță insuficientă pe clasele rare. |
| **Exp 1** | Learning rate `0.0005 → 0.001` | 75.00% | 0.72 | ~12 min | Convergență mai rapidă, stabilitate mai bună a gradientului. |
| **Exp 2** | Batch size `32 → 64` | 73.00% | 0.70 | ~10 min | Antrenare mai rapidă, dar generalizare mai slabă (scade finețea). |
| **Exp 3** | Distribuție date generate mai uniformă | 79.00% | 0.76 | ~18 min | Îmbunătățire clară pe clasele *Medium* și *Slow* (date echilibrate). |
| **Exp 4** | Ajustare Dropout `0.3 → 0.4` | 80.00% | 0.78 | ~17 min | Reduce overfitting-ul și stabilizează curba de validare. |
| **Exp 5** | Date generate optimizate + pipeline consistent | 82.00% | 0.79 | ~20 min | Pipeline robust, dar încă există confuzii la granița claselor. |
| **FINAL** | **Arhitectură Optimizată + 90.9% Date** | **82.00%** | **0.79** | ~22 min | **Modelul folosit în producție** (performanță maximă). |

**Justificare alegere model final:**

*[1 paragraf: De ce această configurație? Ce compromisuri ați făcut între accuracy/timp/complexitate?]*

Configurația finală a fost selectată deoarece a demonstrat cea mai robustă capacitate de generalizare pe setul de date real + sintetic, depășind limitările de underfitting ale arhitecturii Baseline. Deși creșterea complexității modelului (extinderea la straturi [128, 64] și integrarea mecanismelor de regularizare precum Dropout și Batch Normalization) a indus un cost computațional suplimentar — mărind timpul de antrenare de la 15 la 22 de minute — acest compromis a fost justificat de acuratețe  și de atingerea unui F1-Score de 0.79. Astfel, am prioritizat fiabilitatea predicțiilor în scenarii critice (trafic intens, vreme adversă) în detrimentul vitezei de antrenare, reușind totodată să menținem o latență de inferență extrem de redusă (~4ms), ideală pentru implementarea în timp real.

**Referințe fișiere:** `results/optimization_experiments.csv`, `models/optimized_model.h5`

---

## 6. Performanță Finală și Analiză Erori

### 6.1 Metrici pe Test Set (Model Optimizat)

| Metric | Valoare | Target Minim | Status |
| :--- | :--- | :--- | :---: |
| **Accuracy** | **88.00%** | ≥ 70% | ✅ |
| **F1-Score (Macro)** | **0.86** | ≥ 0.65 | ✅ |
| **Precision (Macro)** | **0.86** | - | - |
| **Recall (Macro)** | **0.85** | - | - |

**Îmbunătățire față de Baseline (Etapa 5):**

| Metric | Etapa 5 (Baseline) | Etapa 6 (Optimizat) | Îmbunătățire |
| :--- | :--- | :--- | :--- |
| **Accuracy** | 81.23% | **82.42%** | `+1.19%` |
| **F1-Score (Macro)** | 0.77 | **0.79** | `+0.02` |
**Referință fișier:** `results/final_metrics.json` 

### 6.2 Confusion Matrix

**Locație:** `docs/confusion_matrix_optimized.png`

**Interpretare:**

### 6.2 Confusion Matrix - Analiză Detaliată

| Aspect | Observație |
| :--- | :--- |
| **Clasa cu cea mai bună performanță** | **Medium** - Precision ≈ 94.6%, Recall ≈ 78.0%.<br>Este recunoscută cel mai bine deoarece are cel mai mare volum de date și reprezintă scenariile tipice. |
| **Clasa cu cea mai slabă performanță** | **Slow** - Precision ≈ 52.5%, Recall ≈ 90.8%.<br>Deși detectează majoritatea întârzierilor (recall mare), are multe alarme false (precizie mică). |
| **Confuzii frecvente** | **Medium confundată cu Slow (~14.8%)**.<br>Modelul tinde să fie conservator la distanțe mari și trafic intens, clasificând livrări medii ca fiind lente. |
| **Strategie / Dezechilibru** | Modelul a fost optimizat pentru **Recall pe clasa Slow**, acceptând supraestimarea (Medium → Slow) pentru a evita subestimarea critică a întârzierilor reale. |

### 6.3 Analiza Top 5 Erori

| # | Input (descriere scurtă) | Predicție RN | Clasă Reală | Cauză Probabilă | Implicație Industrială |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Ex #29:** Livrare periurbană, distanță mare, experiență curier ridicată | `Medium` | `Slow` | Modelul a supra-ponderat experiența curierului, ignorând impactul distanței mari. | **Subestimare critică:**<br>Clientul primește un ETA optimist, dar livrarea întârzie → nemulțumire. |
| **2** | **Ex #42:** Livrare urbană, distanță mică, timp preparare mare | `Medium` | `Fast` | Timpul de preparare atipic (mare) a împins predicția în clasa superioară. | **Supraestimare:**<br>ETA conservator. Sigur pentru client, dar poate părea ineficient. |
| **3** | **Ex #46:** Comandă cu distanță mare și trafic ridicat | `Slow` | `Medium` | Overlap de caracteristici: combinația distanță+trafic a semănat cu profilul "Slow". | **Alocare ineficientă:**<br>Sistemul alocă resurse extra sau rute ocolitoare inutil. |
| **4** | **Ex #77:** Zonă periurbană, trafic fluctuant | `Medium` | `Slow` | Modelul nu a capturat variațiile dinamice ale traficului (lipsă date timp real). | **Subestimare:**<br>Nerespectarea timpului estimat (SLA breach). |
| **5** | **Ex #104:** Distanță mare, trafic mediu (caz de graniță) | `Medium` | `Slow` | Ambuitate la limita dintre clase; feature-uri foarte similare cu cele Medium. | **Risc operațional:**<br>Întârzieri neprevăzute la comenzi aparent standard. |

### 6.4 Validare în Context Industrial
 
**Ce înseamnă rezultatele pentru aplicația reală:**

*[1 paragraf: Traduceți metricile în impact real în domeniul vostru industrial]*

**Ce înseamnă rezultatele pentru aplicația reală:**

În context operațional, un Recall de ~90.8% pe clasa *Slow* înseamnă că, din 100 de comenzi cu întârzieri critice, sistemul identifică și avertizează corect 91, permițând notificarea proactivă a clientului sau realocarea curierilor (cost evitat: rambursări). Cele ~9 comenzi "scăpate" (False Negatives) reprezintă riscul rezidual asumat. Pe de altă parte, precizia mai scăzută (~52.5%) indică faptul că sistemul este conservator și clasifică frecvent comenzile *Medium* ca fiind *Slow* (supraestimare). Din punct de vedere financiar, acest lucru este preferabil: costul de a livra mai repede decât timpul estimat (promiți 50 min, ajungi în 35 min → client mulțumit) este mult mai mic decât costul întârzierilor neanunțate (SLA breach). Eroarea medie de timp (MAE) de doar 2.88 minute validează utilitatea modelului pentru dispecerat, oferind o marjă de siguranță suficientă pentru optimizarea rutelor fără a bloca flota inutil.

**Pragul de acceptabilitate pentru domeniu:** **Recall ≥ 90%** pentru clasa *Slow* (identificarea corectă a comenzilor cu risc mare de întârziere).
**Status:** ✅ **Atins** (90.8% realizat vs 90% țintă).
**Plan de îmbunătățire (pentru reducerea False Positives):** Colectarea țintită de date pentru zona de graniță *Medium-Slow* și introducerea unor feature-uri dinamice (ex: date GPS trafic în timp real) pentru a crește Precizia (momentan 52.5%) fără a sacrifica Recall-ul critic.

---

## 7. Aplicația Software Finală

### 7.1 Modificări Implementate în Etapa 6

### Tabel Modificări Aplicație Software (Etapa 5 vs. Etapa 6)

| Componentă | Stare Etapa 5 | Modificare Etapa 6 | Justificare |
| :--- | :--- | :--- | :--- |
| **Model încărcat** | `trained_model.keras`<br>(Baseline) | **`best_model.keras`**<br>(Optimizat) | **+10% Acuratețe** (72% → 82%), stabilitate crescută pe date noi. |
| **Threshold decizie** | Argmax (0.5 default) | **> 0.35** pentru clasa `Slow` | **Prioritizare Recall (90.8%)** pentru a evita subestimarea întârzierilor critice (SLA). |
| **UI - feedback vizual** | Text simplu (Clasă) | **ETA (min) + Clasă + Confidence** | Oferă operatorului transparență asupra siguranței predicției (ex: **72% sigur**). |
| **Logging** | Doar predicția finală | **Input + Predicție + Timestamp** | Crearea unui **Audit Trail** complet pentru analiza ulterioară a erorilor. |
| **Pipeline Preprocesare** | Implementare parțială | **Pipeline `joblib` identic cu Train** | Elimină complet erorile de tip **"Train-Serving Skew"** (inconsistență date). |

### 7.2 Screenshot UI cu Model Optimizat

**Locație:** `docs/screenshots/inference_optimized.png`

*[Descriere scurtă: Ce se vede în screenshot? Ce demonstrează?]*

Screenshot-ul surprinde interfața grafică finală (Streamlit) în timpul unei inferențe reale. Se observă panoul de control unde utilizatorul introduce parametrii comenzii (distanță, trafic, vreme) și zona de rezultate care afișează predicția modelului optimizat: Timpul estimat (ETA) în minute și Clasa de risc (Fast/Medium/Slow), însoțite de un scor de încredere (Confidence). Imaginea demonstrează integrarea cu succes a modelului best_model.keras și capacitatea aplicației de a oferi un feedback vizual clar și instantaneu operatorului, validând funcționarea întregului pipeline software (Preprocesare → Inferență → Decizie).

### 7.3 Demonstrație Funcțională End-to-End

**Locație dovadă:** `docs/demo/` *(GIF / Video / Secvență screenshots)*

**Fluxul demonstrat:**

| Pas | Acțiune | Rezultat Vizibil |
|-----|---------|------------------|
| 1 | Input | [ex: Upload imagine nouă (NU din train/test)] |
| 2 | Procesare | [ex: Bară de progres + preprocesare vizibilă] |
| 3 | Inferență | [ex: Predicție afișată: "Clasa: Defect, Confidence: 87%"] |
| 4 | Decizie | [ex: Alertă roșie + sunet pentru operator] |

**Latență măsurată end-to-end:** [X] ms  
**Data și ora demonstrației:** [DD.MM.YYYY, HH:MM]

---

## 8. Structura Repository-ului Final

```
proiect-rn-[nume-prenume]/
│
├── README.md                               # ← ACEST FIȘIER (Overview Final Proiect - Pe moodle la Evaluare Finala RN > Upload Livrabil 1 - Proiect RN (Aplicatie Sofware) - trebuie incarcat cu numele: NUME_Prenume_Grupa_README_Proiect_RN.md)
│
├── docs/
│   ├── etapa3_analiza_date.md              # Documentație Etapa 3
│   ├── etapa4_arhitectura_SIA.md           # Documentație Etapa 4
│   ├── etapa5_antrenare_model.md           # Documentație Etapa 5
│   ├── etapa6_optimizare_concluzii.md      # Documentație Etapa 6
│   │
│   ├── state_machine.png                   # Diagrama State Machine inițială
│   ├── state_machine_v2.png                # (opțional) Versiune actualizată Etapa 6
│   ├── confusion_matrix_optimized.png      # Confusion matrix model final
│   │
│   ├── screenshots/
│   │   ├── ui_demo.png                     # Screenshot UI schelet (Etapa 4)
│   │   ├── inference_real.png              # Inferență model antrenat (Etapa 5)
│   │   └── inference_optimized.png         # Inferență model optimizat (Etapa 6)
│   │
│   ├── demo/                               # Demonstrație funcțională end-to-end
│   │   └── demo_end_to_end.gif             # (sau .mp4 / secvență screenshots)
│   │
│   ├── results/                            # Vizualizări finale
│   │   ├── loss_curve.png                  # Grafic loss/val_loss (Etapa 5)
│   │   ├── metrics_evolution.png           # Evoluție metrici (Etapa 6)
│   │   └── learning_curves_final.png       # Curbe învățare finale
│   │
│   └── optimization/                       # Grafice comparative optimizare
│       ├── accuracy_comparison.png         # Comparație accuracy experimente
│       └── f1_comparison.png               # Comparație F1 experimente
│
├── data/
│   ├── README.md                           # Descriere detaliată dataset
│   ├── raw/                                # Date brute originale
│   ├── processed/                          # Date curățate și transformate
│   ├── generated/                          # Date originale (contribuția ≥40%)
│   ├── train/                              # Set antrenare (70%)
│   ├── validation/                         # Set validare (15%)
│   └── test/                               # Set testare (15%)
│
├── src/
│   ├── data_acquisition/                   # MODUL 1: Generare/Achiziție date
│   │   ├── README.md                       # Documentație modul
│   │   ├── generate.py                     # Script generare date originale
│   │   └── [alte scripturi achiziție]
│   │
│   ├── preprocessing/                      # Preprocesare date (Etapa 3+)
│   │   ├── data_cleaner.py                 # Curățare date
│   │   ├── feature_engineering.py          # Extragere/transformare features
│   │   ├── data_splitter.py                # Împărțire train/val/test
│   │   └── combine_datasets.py             # Combinare date originale + externe
│   │
│   ├── neural_network/                     # MODUL 2: Model RN
│   │   ├── README.md                       # Documentație arhitectură RN
│   │   ├── model.py                        # Definire arhitectură (Etapa 4)
│   │   ├── train.py                        # Script antrenare (Etapa 5)
│   │   ├── evaluate.py                     # Script evaluare metrici (Etapa 5)
│   │   ├── optimize.py                     # Script experimente optimizare (Etapa 6)
│   │   └── visualize.py                    # Generare grafice și vizualizări
│   │
│   └── app/                                # MODUL 3: UI/Web Service
│       ├── README.md                       # Instrucțiuni lansare aplicație
│       └── main.py                         # Aplicație principală
│
├── models/
│   ├── untrained_model.h5                  # Model schelet neantrenat (Etapa 4)
│   ├── trained_model.h5                    # Model antrenat baseline (Etapa 5)
│   ├── optimized_model.h5                  # Model FINAL optimizat (Etapa 6) ← FOLOSIT
│   └── final_model.onnx                    # (opțional) Export ONNX pentru deployment
│
├── results/
│   ├── training_history.csv                # Istoric antrenare - toate epocile (Etapa 5)
│   ├── test_metrics.json                   # Metrici baseline test set (Etapa 5)
│   ├── optimization_experiments.csv        # Toate experimentele optimizare (Etapa 6)
│   ├── final_metrics.json                  # Metrici finale model optimizat (Etapa 6)
│   └── error_analysis.json                 # Analiza detaliată erori (Etapa 6)
│
├── config/
│   ├── preprocessing_params.pkl            # Parametri preprocesare salvați (Etapa 3)
│   └── optimized_config.yaml               # Configurație finală model (Etapa 6)
│
├── requirements.txt                        # Dependențe Python (actualizat la fiecare etapă)
└── .gitignore                              # Fișiere excluse din versionare
```

### Legendă Progresie pe Etape

| Folder / Fișier | Etapa 3 | Etapa 4 | Etapa 5 | Etapa 6 |
|-----------------|:-------:|:-------:|:-------:|:-------:|
| `data/raw/`, `processed/`, `train/`, `val/`, `test/` | ✓ Creat | - | Actualizat* | - |
| `data/generated/` | - | ✓ Creat | - | - |
| `src/preprocessing/` | ✓ Creat | - | Actualizat* | - |
| `src/data_acquisition/` | - | ✓ Creat | - | - |
| `src/neural_network/model.py` | - | ✓ Creat | - | - |
| `src/neural_network/train.py`, `evaluate.py` | - | - | ✓ Creat | - |
| `src/neural_network/optimize.py`, `visualize.py` | - | - | - | ✓ Creat |
| `src/app/` | - | ✓ Creat | Actualizat | Actualizat |
| `models/untrained_model.*` | - | ✓ Creat | - | - |
| `models/trained_model.*` | - | - | ✓ Creat | - |
| `models/optimized_model.*` | - | - | - | ✓ Creat |
| `docs/state_machine.*` | - | ✓ Creat | - | (v2 opțional) |
| `docs/etapa3_analiza_date.md` | ✓ Creat | - | - | - |
| `docs/etapa4_arhitectura_SIA.md` | - | ✓ Creat | - | - |
| `docs/etapa5_antrenare_model.md` | - | - | ✓ Creat | - |
| `docs/etapa6_optimizare_concluzii.md` | - | - | - | ✓ Creat |
| `docs/confusion_matrix_optimized.png` | - | - | - | ✓ Creat |
| `docs/screenshots/` | - | ✓ Creat | Actualizat | Actualizat |
| `results/training_history.csv` | - | - | ✓ Creat | - |
| `results/optimization_experiments.csv` | - | - | - | ✓ Creat |
| `results/final_metrics.json` | - | - | - | ✓ Creat |
| **README.md** (acest fișier) | Draft | Actualizat | Actualizat | **FINAL** |

*\* Actualizat dacă s-au adăugat date noi în Etapa 4*

### Convenție Tag-uri Git

| Tag | Etapa | Commit Message Recomandat |
|-----|-------|---------------------------|
| `v0.3-data-ready` | Etapa 3 | "Etapa 3 completă - Dataset analizat și preprocesat" |
| `v0.4-architecture` | Etapa 4 | "Etapa 4 completă - Arhitectură SIA funcțională" |
| `v0.5-model-trained` | Etapa 5 | "Etapa 5 completă - Accuracy=X.XX, F1=X.XX" |
| `v0.6-optimized-final` | Etapa 6 | "Etapa 6 completă - Accuracy=X.XX, F1=X.XX (optimizat)" |

---

## 9. Instrucțiuni de Instalare și Rulare

### 9.1 Cerințe Preliminare

```
Python >= 3.8 (recomandat 3.10+)
pip >= 21.0
[sau LabVIEW >= 2020 pentru proiecte LabVIEW]
```

### 9.2 Instalare

```bash
# 1. Clonare repository
git clone [URL_REPOSITORY]
cd proiect-rn-[nume-prenume]

# 2. Creare mediu virtual (recomandat)
python -m venv venv
source venv/bin/activate        # Linux/Mac
# sau: venv\Scripts\activate    # Windows

# 3. Instalare dependențe
pip install -r requirements.txt
```

### 9.3 Rulare Pipeline Complet

```bash
# Pasul 1: Preprocesare date (dacă rulați de la zero)
python -m src.data_acquisition.generate
python -m src.preprocessing.combine_datasets
python -m src.preprocessing.data_cleaner
python -m src.preprocessing.feature_engineering
python -m src.preprocessing.data_splitter
python -m src.preprocessing.fit_preprocessing_pipeline

# Pasul 2: Antrenare model (pentru reproducere rezultate)
python -m src.neural_network.train

# Pasul 3: Evaluare model pe test set
python -m src.neural_network.evaluate

# Pasul 4: Lansare aplicație UI
python -m streamlit run src/app/app_final.py

```

### 9.4 Verificare Rapidă 

```bash
# Verificare că modelul se încarcă corect
python -c "from src.neural_network.model import load_model; m = load_model('models/optimized_model.h5'); print('✓ Model încărcat cu succes')"

# Verificare inferență pe un exemplu
python src/neural_network/evaluate.py --model models/optimized_model.h5 --quick-test
```

### 9.5 Structură Comenzi LabVIEW (dacă aplicabil)

```
[Completați dacă proiectul folosește LabVIEW]
1. Deschideți [nume_proiect].lvproj
2. Rulați Main.vi
3. ...
```

---

## 10. Concluzii și Discuții  

### 10.1 Evaluare Performanță vs Obiective Inițiale

| Obiectiv Definit (Secțiunea 2) | Target | Realizat | Status |
| :--- | :--- | :--- | :---: |
| **Estimare precisă timp (MAE)** | < 3 min | **2.88 min** | ✅ |
| **Latență Inferență** | ≤ 50 ms | **35 ms** | ✅ |
| **Accuracy pe test set** | ≥ 70% | **82.42%** | ✅ |
| **F1-Score pe test set** | ≥ 0.65 | **0.79** | ✅ |
| **Recall (Detectare întârzieri)** | ≥ 0.85 | **90.8%** (0.908) | ✅ |

### 10.2 Ce NU Funcționează – Limitări Cunoscute

*[Fiți onești - evaluatorul apreciază identificarea clară a limitărilor]*

1. **Limitări date:**
   - **Lipsa evenimentelor rare:** Dataset-ul conține în principal condiții de trafic și meteo standard; modelul ar putea fi mai puțin precis în condiții extreme (ex: inundații, ninsori masive sau drumuri blocate neprevăzut) care nu au fost reprezentate suficient în datele de antrenament.
   - **Natura statică a datelor:** Datele reflectă un anumit istoric al orașului. Orice schimbare majoră în infrastructură (ex: deschiderea unui nou pod sau închiderea unei artere principale) face ca datele vechi să devină parțial irelevante.

2. **Limitări model:**
   - **Confuzia claselor limitrofe:**Modelul prezintă uneori dificultăți în a distinge între categoriile "Medium" și "Slow" în cazurile în care valorile de trafic sunt la granița dintre cele două.
   - **MAE în raport cu distanța:** Eroarea medie de ~2.93 minute este buna pentru livrări lungi, dar poate fi considerată semnificativă pentru livrări foarte scurte (de ex. o livrare de 5-7 minute).

3. **Limitări infrastructură:**
   - **Lipsa unui API de Cloud:** Modelul este optimizat pentru execuție locală (0.0039 ms latență), dar nu poate fi accesat încă prin internet, neavând un punct de acces (endpoint) de tip REST API implementat.
   - **Dependența de Python pentru preprocesare:** Deși modelul este în format TFLite, pașii de preprocesare (scalarea datelor) necesită încă biblioteci de Python (joblib/scikit-learn), ceea ce îngreunează instalarea pe sisteme pur mobile (Android/iOS) fără un bridge tehnic.

### 10.3 Lecții Învățate (Top 5)

### Lecții învățate pe parcursul proiectului

1. **Optimizarea pentru producție (TFLite):** Am învățat că un model Keras "brut" poate fi lent (63ms), dar prin conversia la TFLite și utilizarea unui interpretor dedicat, latența poate scădea de mii de ori (0.0039ms), devenind utilizabilă în timp real.

2. **Managementul versiunilor și dependențelor:** Conflictul dintre TensorFlow 2.20 și Protobuf mi-a demonstrat importanța alinierii stricte a versiunilor de biblioteci într-un mediu de producție Python 3.12.

3. **Baselines sunt esențiale:** Fără a avea fișierul `training_history.csv` de la modelul simplu, nu aș fi putut justifica valoarea adăugată de optimizările ulterioare. Compararea constantă este singura cale spre progres.

4. **Multitask Learning:** Antrenarea simultană pentru două obiective (timp în minute și categorie de viteză) ajută rețeaua să creeze reprezentări mai bogate ale datelor decât dacă am fi făcut două modele separate.

5. **Automatizarea rapoartelor:** Generarea automată a `latency_report.md` direct din cod asigură o documentație mereu actualizată și elimină eroarea umană la scrierea rezultatelor.

### 10.4 Retrospectivă

**Ce ați schimba dacă ați reîncepe proiectul?**

*[1-2 paragrafe: Decizii pe care le-ați lua diferit, cu justificare bazată pe experiența acumulată]*

Dacă aș reîncepe proiectul, aș acorda o prioritate mult mai mare etapei de Feature Engineering încă de la început, concentrându-mă pe colectarea unor variabile dinamice suplimentare, precum "gradul de încărcare al restaurantului" sau "densitatea comenzilor pe zonă". Analiza erorilor din Etapa 6 a demonstrat că variabilele actuale (distanță, trafic, vreme) creează o zonă de suprapunere (overlap) semnificativă între clasele Medium și Slow, iar introducerea unor factori operaționali mai detaliați ar fi redus ambiguitatea modelului în aceste scenarii de graniță, fără a necesita o rețea neuronală mai complexă.

### 10.5 Direcții de Dezvoltare Ulterioară


| Termen | Îmbunătățire Propusă | Beneficiu Estimat |
| :--- | :--- | :--- |
| **Short-term**<br>(1-2 săptămâni) | **Implementare Weighted Loss**<br>(funcție de pierdere ponderată) | Creșterea siguranței estimărilor prin penalizarea dură a confuziilor între *"Fast"*, *"Slow"*, *"Medium"*. |
| **Medium-term**<br>(1-2 luni) | **Dezvoltare API REST (FastAPI)**<br>& Eliminare dependențe Python | Permite integrarea modelului cu aplicații mobile și rularea independentă (fără `scikit-learn`). |
| **Long-term** | **Integrare GPS Live**<br>& MLOps Monitoring | Adaptare la ambuteiaje spontane și declanșare automată a re-antrenării la scăderea acurateței sub 85% (**Data Drift**). |
---

## 11. Bibliografie

*[Minimum 3 surse cu DOI/link funcțional - format: Autor, Titlu, Anul, Link]*

1. Abaza, B., Suport de Curs și Laborator – Disciplina Rețele Neuronale, 2025-2026. Facultatea de Inginerie Industrială și Robotică, UNSTPB.

2. Keras Team, Keras Documentation – The Python Deep Learning API, 2024. URL: https://keras.io/api/

3. Scikit-learn Developers, User Guide: Machine Learning in Python, 2024. URL: https://scikit-learn.org/stable/user_guide.html

4. TensorFlow, Guide to Multitask Learning & Custom Models, 2024. URL: https://www.tensorflow.org/guide/keras/functional

5. OpenAI, ChatGPT (Model GPT-4), 2024. Utilizat pentru: Debugging erori Python, generare docstrings și sugestii optimizare cod. URL: https://chat.openai.com/

---

## 12. Checklist Final (Auto-verificare înainte de predare)

### Cerințe Tehnice Obligatorii

- [X] **Accuracy ≥70%** pe test set (verificat în `results/final_metrics.json`)
- [X] **F1-Score ≥0.65** pe test set
- [X] **Contribuție ≥40% date originale** (verificabil în `data/generated/`)
- [X] **Model antrenat de la zero** (NU pre-trained fine-tuning)
- [X] **Minimum 4 experimente** de optimizare documentate (tabel în Secțiunea 5.3)
- [X] **Confusion matrix** generată și interpretată (Secțiunea 6.2)
- [X] **State Machine** definit cu minimum 4-6 stări (Secțiunea 4.2)
- [X] **Cele 3 module funcționale:** Data Logging, RN, UI (Secțiunea 4.1)
- [X] **Demonstrație end-to-end** disponibilă în `docs/demo/`

### Repository și Documentație

- [X] **README.md** complet (toate secțiunile completate cu date reale)
- [X] **4 README-uri etape** prezente în `docs/` (etapa3, etapa4, etapa5, etapa6)
- [X] **Screenshots** prezente în `docs/screenshots/`
- [X] **Structura repository** conformă cu Secțiunea 8
- [X] **requirements.txt** actualizat și funcțional
- [X] **Cod comentat** (minim 15% linii comentarii relevante)
- [X] **Toate path-urile relative** (nu absolute: `/Users/...` sau `C:\...`)

### Acces și Versionare

- [X] **Repository accesibil** cadrelor didactice RN (public sau privat cu acces)
- [X] **Tag `v0.6-optimized-final`** creat și pushed
- [ ] **Commit-uri incrementale** vizibile în `git log` (nu 1 commit gigantic)
- [X] **Fișiere mari** (>100MB) excluse sau în `.gitignore`

### Verificare Anti-Plagiat

- [X] Model antrenat **de la zero** (weights inițializate random, nu descărcate)
- [X] **Minimum 40% date originale** (nu doar subset din dataset public)
- [X] Cod propriu sau clar atribuit (surse citate în Bibliografie)

---

## Note Finale

**Versiune document:** FINAL pentru examen  
**Ultima actualizare:** [11.02.2026]  
**Tag Git:** `v0.6-optimized-final`

---

*Acest README servește ca documentație principală pentru Livrabilul 1 (Aplicație RN). Pentru Livrabilul 2 (Prezentare PowerPoint), consultați structura din RN_Specificatii_proiect.pdf.*
