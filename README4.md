# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** [Belu Maria Alexandra]  
**Link Repository GitHub** https://github.com/belualexandra/Retele-Neuronale.git
**Data:** [09.12.2025]  
---

## Scopul Etapei 4

Această etapă corespunde punctului **5. Dezvoltarea arhitecturii aplicației software bazată pe RN** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.

**Trebuie să livrați un SCHELET COMPLET și FUNCȚIONAL al întregului Sistem cu Inteligență Artificială (SIA). In acest stadiu modelul RN este doar definit și compilat (fără antrenare serioasă).**

### IMPORTANT - Ce înseamnă "schelet funcțional":

 **CE TREBUIE SĂ FUNCȚIONEZE:**
- Toate modulele pornesc fără erori
- Pipeline-ul complet rulează end-to-end (de la date → până la output UI)
- Modelul RN este definit și compilat (arhitectura există)
- Web Service/UI primește input și returnează output

 **CE NU E NECESAR ÎN ETAPA 4:**
- Model RN antrenat cu performanță bună
- Hiperparametri optimizați
- Acuratețe mare pe test set
- Web Service/UI cu funcționalități avansate

**Scopul anti-plagiat:** Nu puteți copia un notebook + model pre-antrenat de pe internet, pentru că modelul vostru este NEANTRENAT în această etapă. Demonstrați că înțelegeți arhitectura și că ați construit sistemul de la zero.

---

##  Livrabile Obligatorii

### 1. Tabelul Nevoie Reală → Soluție SIA → Modul Software (max ½ pagină)
Completați in acest readme tabelul următor cu **minimum 2-3 rânduri** care leagă nevoia identificată în Etapa 1-2 cu modulele software pe care le construiți (metrici măsurabile obligatoriu):

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul vostru** | **Modul software responsabil** |
|---------------------------|---------------------------------|--------------------------------|
| Ex: Detectarea automată a fisurilor în suduri robotizate | Clasificare imagine radiografică → alertă operator în < 2 secunde | RN + Web Service |
| Ex: Predicția uzurii lagărelor în turbine eoliene | Analiză vibrații în timp real → alertă preventivă cu 95% acuratețe | Data Logging + RN + UI |
| Ex: Optimizarea traiectoriilor robotului mobil în depozit | Predicție timp traversare → reducere 20% consum energetic | RN + Control Module |
| [Completați cu proiectul vostru] | | |
| [Completați cu proiectul vostru] | | |


| **Nevoie reală concretă**                                                                                | **Cum o rezolvă SIA-ul vostru (Sistem IA)**                                                                                               | **Modul software responsabil**                        |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Estimarea timpului de livrare pentru comenzile de mâncare, în condiții dinamice (trafic, vreme, vehicul) | Rețeaua neuronală prezice timpul de livrare cu o eroare medie țintă < **±5 minute**, folosind date istorice + date generate               | Modul 1 (Data Acquisition) + Modul 2 (Neural Network) |
| Furnizarea unui timp de livrare realist către client pentru a crește satisfacția și transparența         | Interfața Web afișează instant predicția modelului → reducere a incertitudinii clientului cu > **30%**                                    | Modul 3 (Web Service / UI)                            |
| Reducerea întârzierilor generate de estimări eronate ale curierilor sau ale restaurantelor               | Modelul IA integrează factori reali (distanță, vreme, trafic, experiență) → estimări mai stabile decât euristicile obișnuite (±10–15 min) | Modul 2 (Neural Network)                              |
| Analiza impactului factorilor externi asupra timpului de livrare (pentru optimizarea logisticii)         | Sistemul IA poate simula scenarii „What-if” (ex.: trafic mare, ploaie, vehicul diferit) → permite optimizări cu **5–15%**                 | Modul 1 (Data Acquisition) + Modul 2 (RN)             |


**Instrucțiuni:**
- Fiți concreti (nu vagi): "detectare fisuri sudură" ✓, "îmbunătățire proces" ✗
- Specificați metrici măsurabile: "< 2 secunde", "> 95% acuratețe", "reducere 20%"
- Legați fiecare nevoie de modulele software pe care le dezvoltați

---

### 2. Contribuția Voastră Originală la Setul de Date – MINIM 40% din Totalul Observațiilor Finale

**Regula generală:** Din totalul de **N observații finale** în `data/processed/`, **minimum 40%** trebuie să fie **contribuția voastră originală**.

#### Cum se calculează 40%:

**Exemplu 1 - Dataset DOAR public în Etapa 3:**
```
Etapa 3: Ați folosit 10,000 samples dintr-o sursa externa (ex: Kaggle)
Etapa 4: Trebuie să generați/achiziționați date astfel încât:
  
Opțiune A: Adăugați 6,666 samples noi → Total 16,666 (6,666/16,666 = 40%)
Opțiune B: Păstrați 6,000 publice + 4,000 generate → Total 10,000 (4,000/10,000 = 40%)
```

**Exemplu 2 - Dataset parțial original în Etapa 3:**
```
Etapa 3: Ați avut deja 3,000 samples generate + 7,000 publice = 10,000 total
Etapa 4: 3,000 samples existente numără ca "originale"
        Dacă 3,000/10,000 = 30% < 40% → trebuie să generați încă ~1,700 samples
        pentru a ajunge la 4,700/10,000 = 47% > 40% ✓
```

**Exemplu 3 - Dataset complet original:**
```
Etapa 3-4: Generați toate datele (simulare, senzori proprii, etichetare manuală - varianta recomandata)
           → 100% original ✓ (depășește cu mult 40% - FOARTE BINE!)
```

#### Tipuri de contribuții acceptate (exemple din inginerie):

Alegeți UNA sau MAI MULTE dintre variantele de mai jos și **demonstrați clar în repository**:

| **Tip contribuție** | **Exemple concrete din inginerie** | **Dovada minimă cerută** |
|---------------------|-------------------------------------|--------------------------|
| **Date generate prin simulare fizică** | • Traiectorii robot în Gazebo<br>• Vibrații motor cu zgomot aleator calibrat<br>• Consumuri energetice proces industrial simulat | Cod Python/LabVIEW funcțional + grafice comparative (simulat vs real din literatură) + justificare parametri |
| **Date achiziționate cu senzori proprii** | • 500-2000 măsurători accelerometru pe motor<br>• 100-1000 imagini capturate cu cameră montată pe robot<br>• 200-1000 semnale GPS/IMU de pe platformă mobilă<br>• Temperaturi/presiuni procesate din Arduino/ESP32 | Foto setup experimental + CSV-uri produse + descriere protocol achiziție (frecvență, durata, condiții) |
| **Etichetare/adnotare manuală** | • Etichetat manual 1000+ imagini defecte sudură<br>• Anotat 500+ secvențe video cu comportamente robot<br>• Clasificat manual 2000+ semnale vibrații (normal/anomalie)<br>• Marcat manual 1500+ puncte de interes în planuri tehnice | Fișier Excel/JSON cu labels + capturi ecran tool etichetare + log timestamp-uri lucru |
| **Date sintetice prin metode avansate** | • Simulări FEM/CFD pentru date dinamice proces | Cod implementare metodă + exemple before/after + justificare hiperparametri + validare pe subset real |

#### Declarație obligatorie în README:

Scrieți clar în acest README (Secțiunea 2):

```markdown
### Contribuția originală la setul de date:

**Total observații finale:** [1700] (1000 observații reale din Kaggle + 700 observații generate în Etapa 4)
**Observații originale:** [700] ([41]%)

**Tipul contribuției:**
[X] Date generate prin simulare fizică  
[ ] Date achiziționate cu senzori proprii  
[ ] Etichetare/adnotare manuală  
[ ] Date sintetice prin metode avansate  

**Descriere detaliată:**
[Explicați în 2-3 paragrafe cum ați generat datele, ce metode ați folosit, 
de ce sunt relevante pentru problema voastră, cu ce parametri ați rulat simularea/achiziția]

Pentru a asigura contribuția personală asupra datasetului și pentru a depăși pragul de 40% date originale cerut în Etapa 4, am dezvoltat un modul de simulare care generează 700 de observații sintetice privind livrarea comenzilor de mâncare. Simularea reproduce comportamentul real al procesului de livrare folosind un model matematic inspirat din factori observați în datasetul Kaggle, precum și din logică fizică și operațională a serviciilor de livrare. Parametrii utilizați includ: distanța până la client, nivelul traficului, condițiile meteo, momentul zilei, tipul vehiculului, timpul de preparare și experiența curierului. Acești factori sunt combinați într-o ecuație care estimează timpul final de livrare, aplicând penalizări și ajustări realiste pentru condiții dificile (trafic intens, vreme nefavorabilă, vehicul lent sau experiență redusă).

Metoda de simulare folosită este una hibridă: valorile pentru fiecare feature sunt eșantionate din distribuții controlate (uniforme sau discrete), în timp ce timpul de livrare este calculat printr-un model semi-fizic. Acest model folosește o componentă deterministă (timp bazat pe distanță și factor de viteză) combinată cu componente stocastice (zgomot aleatoriu și variații contextuale), asigurând astfel diversitate realistă în date. Parametrii (intervale, penalizări, factori de scalare) au fost calibrați astfel încât distribuția rezultată să fie comparabilă cu cea a datelor reale, ceea ce este confirmat prin statisticile și graficele comparative incluse în modul.

Datele generate sunt relevante deoarece imită comportamentul real al livrărilor urbane, reproduc relațiile dintre distanță și timp, precum și efectele condițiilor externe asupra performanței curierilor. Acest lucru permite rețelei neuronale să fie antrenată pe un set îmbogățit, variat și mai robust, reducând riscul de overfitting pe un singur tip de date. Simularea oferă astfel un cadru controlat în care pot fi incluse scenarii rare sau extreme (ex: ninsoare, trafic foarte ridicat), care sunt subreprezentate în datele reale, dar importante pentru generalizarea modelului.


**Locația codului:** `src/data_acquisition/generate_data.py`
**Locația datelor:** `data/generated/generated_deliveries.csv`

**Dovezi:**
- Grafic comparativ: `docs/generated_vs_real.png`
- Setup experimental: `docs/acquisition_setup.jpg` 
- Tabel statistici: `docs/data_statistics.csv`
- Grafice suplimentare incluse ca dovadă extinsă: 
`docs/hist_delivery_time_compare.png`
`docs/boxplot_delivery_time_compare.png`
`docs/scatter_distance_delivery_compare.png`
`docs/barchart_mean_delivery_time.png`
`docs/scatter_prep_vs_delivery_compare.png`
`docs/scatter_experience_vs_delivery_compare.png`
Aceste grafice suplimentare evidențiază faptul că relațiile funcționale dintre variabilele de intrare și timpul de livrare (ex: distanță → timp, experiență → viteză, trafic → penalizări) sunt păstrate atât în datasetul original, cât și în cel generat, validând astfel consistența simulării.


#### Exemple pentru "contribuție originală":
-Simulări fizice realiste cu ecuații și parametri justificați  
-Date reale achiziționate cu senzori proprii (setup documentat)  
-Augmentări avansate cu justificare fizică (ex: simulare perspective camera industrială)  


#### Atenție - Ce NU este considerat "contribuție originală":

- Augmentări simple (rotații, flips, crop) pe date publice  
- Aplicare filtre standard (Gaussian blur, contrast) pe imagini publice  
- Normalizare/standardizare (aceasta e preprocesare, nu generare)  
- Subset dintr-un dataset public (ex: selectat 40% din ImageNet)


---

### 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)

**Cerințe:**
- **Minimum 4-6 stări clare** cu tranziții între ele
- **Formate acceptate:** PNG/SVG, pptx, draw.io 
- **Locație:** `docs/state_machine.*` (orice extensie)
- **Legendă obligatorie:** 1-2 paragrafe în acest README: "De ce ați ales acest State Machine pentru nevoia voastră?"


### Justificarea State Machine-ului ales


Am ales o arhitectură de tip flux secvențial interactiv, deoarece sistemul meu de predicție a timpului de livrare funcționează într-un mod user-centric: utilizatorul introduce datele necesare, iar aplicația procesează aceste informații pas cu pas (achiziție → preprocesare → inferență) și returnează o predicție. Structura este perfect aliniată cu cerințele unui Sistem cu Inteligență Artificială (SIA), în care fiecare modul are un rol clar și există mecanisme de gestionare a erorilor.

### Stările principale din State Machine

# INIT
Sistemul inițializează resursele: încarcă modelul RN, preprocessorul, verifică existența fișierelor necesare și confirmă că aplicația poate funcționa. Dacă inițializarea reușește, trece în IDLE; dacă apare o eroare, trece în ERROR, de unde poate reveni în INIT prin reset.

# IDLE

Este starea de repaus în care sistemul așteaptă interacțiunea utilizatorului. De aici pot apărea două tranziții:
buton Start → ACQUIRE_DATA
buton Stop → STOP (închiderea aplicației)

# ACQUIRE_DATA

Sunt colectate datele introduse de utilizator (distanță, trafic, vreme, tip vehicul etc.).
Tranziții posibile:

date OK → PREPROCESS
eroare date → ERROR
oprire de urgență → STOP

# PREPROCESS

Datele brute sunt transformate cu preprocessor.pkl (scalare + One-Hot Encoding).
Tranziții:
preprocesare OK → INFERENCE
eroare preprocesare → ERROR
oprire de urgență → STOP

# INFERENCE

Modelul neuronal calculează timpul estimat de livrare pe baza datelor preprocesate.
Tranziții:
inferință finalizată → DISPLAY_RESULT
oprire de urgență → STOP

# DISPLAY_RESULT

Rezultatul este afișat utilizatorului, iar sistemul poate:
reveni în IDLE pentru o nouă predicție (continuare monitorizare)
trece în STOP dacă utilizatorul apasă butonul Stop

# ERROR

Stare specială pentru gestionarea problemelor precum:
input invalid
fișiere lipsă
model corupt
erori în preprocesare
Tranziții:
reset → IDLE
oprire sistem → STOP

# STOP

Stare finală în care sistemul se oprește complet și eliberează resursele. Poate apărea din aproape toate stările (oprire cerută de utilizator sau oprire de urgență).

### Tranziții critice 

INIT → IDLE: încărcarea modelului și a preprocessorului a avut succes.

INIT → ERROR: eroare de inițializare; ERROR → INIT prin reset.

IDLE → ACQUIRE_DATA: utilizatorul apasă Start.

IDLE → STOP: utilizatorul apasă Stop.

ACQUIRE_DATA → PREPROCESS: datele sunt valide.

ACQUIRE_DATA → ERROR: date lipsă sau greșite.

ACQUIRE_DATA → STOP: oprire de urgență.

PREPROCESS → INFERENCE: preprocesarea a reușit.

PREPROCESS → ERROR: eroare de scalare/encoding.

PREPROCESS → STOP: oprire de urgență.

INFERENCE → DISPLAY_RESULT: modelul returnează predicția.

INFERENCE → STOP: oprire de urgență.

DISPLAY_RESULT → IDLE: continuare (utilizatorul dorește o nouă predicție).

DISPLAY_RESULT → STOP: utilizatorul apasă Stop.

ERROR → IDLE: utilizatorul apasă reset.

ERROR → STOP: oprire sistem.

### De ce este potrivit acest State Machine?

Această arhitectură respectă fidel modul în care funcționează un sistem real de predicție în domeniul livrărilor: datele sunt introduse de utilizator, validate, preprocesate și analizate de model. Structura în stări permite:

control clar asupra fluxului de date,
gestionarea erorilor la fiecare pas,
siguranță operațională prin oprire de urgență,
posibilitatea de a reporni ciclul oricând (IDLE).

Este o arhitectură robustă, modulară și scalabilă — exact ce se cere într-un proiect de inginerie bazat pe IA.

**Stări tipice pentru un SIA:**
```
IDLE → ACQUIRE_DATA → PREPROCESS → INFERENCE → DISPLAY/ACT → LOG → [ERROR] → STOP
                ↑______________________________________________|
```

**Exemple concrete per domeniu de inginerie:**

#### A. Monitorizare continuă proces industrial (vibrații motor, temperaturi, presiuni):
```
IDLE → START_ACQUISITION → COLLECT_SENSOR_DATA → BUFFER_CHECK → 
PREPROCESS (filtrare, FFT) → RN_INFERENCE → THRESHOLD_CHECK → 
  ├─ [Normal] → LOG_RESULT → UPDATE_DASHBOARD → COLLECT_SENSOR_DATA (loop)
  └─ [Anomalie] → TRIGGER_ALERT → NOTIFY_OPERATOR → LOG_INCIDENT → 
                  COLLECT_SENSOR_DATA (loop)
       ↓ [User stop / Emergency]
     SAFE_SHUTDOWN → STOP
```

#### B. Clasificare imagini defecte producție (suduri, suprafețe, piese):
```
IDLE → WAIT_TRIGGER (senzor trecere piesă) → CAPTURE_IMAGE → 
VALIDATE_IMAGE (blur check, brightness) → 
  ├─ [Valid] → PREPROCESS (resize, normalize) → RN_INFERENCE → 
              CLASSIFY_DEFECT → 
                ├─ [OK] → LOG_OK → CONVEYOR_PASS → IDLE
                └─ [DEFECT] → LOG_DEFECT → TRIGGER_REJECTION → IDLE
  └─ [Invalid] → ERROR_IMAGE_QUALITY → RETRY_CAPTURE (max 3×) → IDLE
       ↓ [Shift end]
     GENERATE_REPORT → STOP
```

#### C. Predicție traiectorii robot mobil (AGV, AMR în depozit):
```
IDLE → LOAD_MAP → RECEIVE_TARGET → PLAN_PATH → 
VALIDATE_PATH (obstacle check) →
  ├─ [Clear] → EXECUTE_SEGMENT → ACQUIRE_SENSORS (LIDAR, IMU) → 
              RN_PREDICT_NEXT_STATE → UPDATE_TRAJECTORY → 
                ├─ [Target reached] → STOP_AT_TARGET → LOG_MISSION → IDLE
                └─ [In progress] → EXECUTE_SEGMENT (loop)
  └─ [Obstacle detected] → REPLAN_PATH → VALIDATE_PATH
       ↓ [Emergency stop / Battery low]
     SAFE_STOP → LOG_STATUS → STOP
```

#### D. Predicție consum energetic (turbine eoliene, procese batch):
```
IDLE → LOAD_HISTORICAL_DATA → ACQUIRE_CURRENT_CONDITIONS 
(vânt, temperatură, demand) → PREPROCESS_FEATURES → 
RN_FORECAST (24h ahead) → VALIDATE_FORECAST (sanity checks) →
  ├─ [Valid] → DISPLAY_FORECAST → UPDATE_CONTROL_STRATEGY → 
              LOG_PREDICTION → WAIT_INTERVAL (1h) → 
              ACQUIRE_CURRENT_CONDITIONS (loop)
  └─ [Invalid] → ERROR_FORECAST → USE_FALLBACK_MODEL → LOG_ERROR → 
                ACQUIRE_CURRENT_CONDITIONS (loop)
       ↓ [User request report]
     GENERATE_DAILY_REPORT → STOP
```

**Notă pentru proiecte simple:**
Chiar dacă aplicația voastră este o clasificare simplă (user upload → classify → display), trebuie să modelați fluxul ca un State Machine. Acest exercițiu vă învață să gândiți modular și să anticipați toate stările posibile (inclusiv erori).

**Legendă obligatorie (scrieți în README):**
```markdown
### Justificarea State Machine-ului ales:

Am ales arhitectura [descrieți tipul: monitorizare continuă / clasificare la senzor / 
predicție batch / control în timp real] pentru că proiectul nostru [explicați nevoia concretă 
din tabelul Secțiunea 1].

Stările principale sunt:
1. [STARE_1]: [ce se întâmplă aici - ex: "achiziție 1000 samples/sec de la accelerometru"]
2. [STARE_2]: [ce se întâmplă aici - ex: "calcul FFT și extragere 50 features frecvență"]
3. [STARE_3]: [ce se întâmplă aici - ex: "inferență RN cu latență < 50ms"]
...

Tranzițiile critice sunt:
- [STARE_A] → [STARE_B]: [când se întâmplă - ex: "când buffer-ul atinge 1024 samples"]
- [STARE_X] → [ERROR]: [condiții - ex: "când senzorul nu răspunde > 100ms"]

Starea ERROR este esențială pentru că [explicați ce erori pot apărea în contextul 
aplicației voastre industriale - ex: "senzorul se poate deconecta în mediul industrial 
cu vibrații și temperatură variabilă, trebuie să gestionăm reconnect automat"].

Bucla de feedback [dacă există] funcționează astfel: [ex: "rezultatul inferenței 
actualizează parametrii controlerului PID pentru reglarea vitezei motorului"].
```

---

### 4. Scheletul Complet al celor 3 Module Cerute la Curs (slide 7)

Toate cele 3 module trebuie să **pornească și să ruleze fără erori** la predare. Nu trebuie să fie perfecte, dar trebuie să demonstreze că înțelegeți arhitectura.

| **Modul** | **Python (exemple tehnologii)** | **LabVIEW** | **Cerință minimă funcțională (la predare)** |
|-----------|----------------------------------|-------------|----------------------------------------------|
| **1. Data Logging / Acquisition** | `src/data_acquisition/` | LLB cu VI-uri de generare/achiziție | **MUST:** Produce CSV cu datele voastre (inclusiv cele 40% originale). Cod rulează fără erori și generează minimum 100 samples demonstrative. |
| **2. Neural Network Module** | `src/neural_network/model.py` sau folder dedicat | LLB cu VI-uri RN | **MUST:** Modelul RN definit, compilat, poate fi încărcat. **NOT required:** Model antrenat cu performanță bună (poate avea weights random/inițializați). |
| **3. Web Service / UI** | Streamlit, Gradio, FastAPI, Flask, Dash | WebVI sau Web Publishing Tool | **MUST:** Primește input de la user și afișează un output. **NOT required:** UI frumos, funcționalități avansate. |

#### Detalii per modul:

#### **Modul 1: Data Logging / Acquisition**

**Funcționalități obligatorii:**
- [X] Cod rulează fără erori: `python src/data_acquisition/generate.py` sau echivalent LabVIEW
- [X] Generează CSV în format compatibil cu preprocesarea din Etapa 3
- [X] Include minimum 40% date originale în dataset-ul final
- [X] Documentație în cod: ce date generează, cu ce parametri

#### **Modul 2: Neural Network Module**

**Funcționalități obligatorii:**
- [X] Arhitectură RN definită și compilată fără erori
- [X] Model poate fi salvat și reîncărcat
- [X] Include justificare pentru arhitectura aleasă (în docstring sau README)
- [X] **NU trebuie antrenat** cu performanță bună (weights pot fi random)


#### **Modul 3: Web Service / UI**

**Funcționalități MINIME obligatorii:**
- [X] Propunere Interfață ce primește input de la user (formular, file upload, sau API endpoint)
- [X] Includeți un screenshot demonstrativ în `docs/screenshots/`

**Ce NU e necesar în Etapa 4:**
- UI frumos/profesionist cu grafică avansată
- Funcționalități multiple (istorice, comparații, statistici)
- Predicții corecte (modelul e neantrenat, e normal să fie incorect)
- Deployment în cloud sau server de producție

**Scop:** Prima demonstrație că pipeline-ul end-to-end funcționează: input user → preprocess → model → output.


## Structura Repository-ului la Finalul Etapei 4 (OBLIGATORIE)

**Verificare consistență cu Etapa 3:**

```
proiect-rn-[nume-prenume]/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── generated/  # Date originale
│   ├── train/
│   ├── validation/
│   └── test/
├── src/
│   ├── data_acquisition/
│   ├── preprocessing/  # Din Etapa 3
│   ├── neural_network/
│   └── app/  # UI schelet
├── docs/
│   ├── state_machine.*           #(state_machine.png sau state_machine.pptx sau state_machine.drawio)
│   └── [alte dovezi]
├── models/  # Untrained model
├── config/
├── README.md
├── README_Etapa3.md              # (deja existent)
├── README_Etapa4_Arhitectura_SIA.md              # ← acest fișier completat (în rădăcină)
└── requirements.txt  # Sau .lvproj
```

**Diferențe față de Etapa 3:**
- Adăugat `data/generated/` pentru contribuția dvs originală
- Adăugat `src/data_acquisition/` - MODUL 1
- Adăugat `src/neural_network/` - MODUL 2
- Adăugat `src/app/` - MODUL 3
- Adăugat `models/` pentru model neantrenat
- Adăugat `docs/state_machine.png` - OBLIGATORIU
- Adăugat `docs/screenshots/` pentru demonstrație UI

---

## Checklist Final – Bifați Totul Înainte de Predare

### Documentație și Structură
- [X] Tabelul Nevoie → Soluție → Modul complet (minimum 2 rânduri cu exemple concrete completate in README_Etapa4_Arhitectura_SIA.md)
- [X] Declarație contribuție 40% date originale completată în README_Etapa4_Arhitectura_SIA.md
- [X] Cod generare/achiziție date funcțional și documentat
- [X] Dovezi contribuție originală: grafice + log + statistici în `docs/`
- [X] Diagrama State Machine creată și salvată în `docs/state_machine.*`
- [X] Legendă State Machine scrisă în README_Etapa4_Arhitectura_SIA.md (minimum 1-2 paragrafe cu justificare)
- [X] Repository structurat conform modelului de mai sus (verificat consistență cu Etapa 3)

### Modul 1: Data Logging / Acquisition
- [X] Cod rulează fără erori (`python src/data_acquisition/...` sau echivalent LabVIEW)
- [X] Produce minimum 40% date originale din dataset-ul final
- [X] CSV generat în format compatibil cu preprocesarea din Etapa 3
- [X] Documentație în `src/data_acquisition/README.md` cu:
  - [X] Metodă de generare/achiziție explicată
  - [X] Parametri folosiți (frecvență, durată, zgomot, etc.)
  - [X] Justificare relevanță date pentru problema voastră
- [X] Fișiere în `data/generated/` conform structurii

### Modul 2: Neural Network
- [X] Arhitectură RN definită și documentată în cod (docstring detaliat) - versiunea inițială 
- [X] README în `src/neural_network/` cu detalii arhitectură curentă

### Modul 3: Web Service / UI
- [X] Propunere Interfață ce pornește fără erori (comanda de lansare testată)
- [X] Screenshot demonstrativ în `docs/screenshots/ui_demo.png`
- [X] README în `src/app/` cu instrucțiuni lansare (comenzi exacte)

---

**Predarea se face prin commit pe GitHub cu mesajul:**  
`"Etapa 4 completă - Arhitectură SIA funcțională"`

**Tag obligatoriu:**  
`git tag -a v0.4-architecture -m "Etapa 4 - Skeleton complet SIA"`


