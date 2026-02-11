# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** [Belu Maria Alexandra]  
**Link Repository GitHub** [ https://github.com/belualexandra/Retele-Neuronale.git ]  
**Data:** [9 decembrie 2025]  
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

| **Nevoie reală concretă**                                                                                                    | **Cum o rezolvă SIA-ul vostru**                                                                                                                                                                                                  | **Modul software responsabil**                    |
| ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Estimarea realistă a timpului de livrare pentru comenzile de mâncare, pentru a evita întârzierile și nemulțumirea clienților | Sistemul SIA prezice timpul de livrare în minute, pe baza distanței, condițiilor de trafic, vremii, momentului zilei și experienței curierului, cu o eroare medie sub **±3 minute (MAE ≈ 2.88)**                                  | Preprocesare date + Rețea Neuronală (Regresie)    |
| Clasificarea comenzilor în funcție de urgență (livrare rapidă / medie / lentă) pentru prioritizarea livrărilor               | Rețeaua neuronală clasifică comenzile în 3 clase (fast / medium / slow), obținând **F1-score macro ≈ 0.80**, permițând sistemului să acorde prioritate comenzilor critice                                                        | Rețea Neuronală (Clasificare multi-clasă)         |
| Integrarea predicției într-o aplicație utilizabilă de operator sau client final                                              | Aplicația web permite introducerea manuală a datelor unei comenzi și afișează instant timpul estimat de livrare și clasa comenzii, folosind **același pipeline de preprocesare ca la antrenare**, eliminând erorile de inferență | Aplicație Web (Streamlit) + Pipeline de inferență |


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

**Total observații finale:** [11000] (după Etapa 3 + Etapa 4)
**Observații originale:** [10000] ([90.9]%)

**Tipul contribuției:**
[ ] Date generate prin simulare fizică  
[ ] Date achiziționate cu senzori proprii  
[ ] Etichetare/adnotare manuală  
[X] Date sintetice prin metode avansate  (Date sintetice generate prin metode controlate (simulare parametrică realistă))

**Descriere detaliată:**
[Explicați în 2-3 paragrafe cum ați generat datele, ce metode ați folosit, 
de ce sunt relevante pentru problema voastră, cu ce parametri ați rulat simularea/achiziția]


În cadrul Etapei 4, setul de date public utilizat inițial a fost extins prin generarea unui volum semnificativ de date sintetice originale, cu scopul de a simula comportamentul real al procesului de livrare a comenzilor de mâncare. Datele au fost generate printr-un script Python dedicat, care modelează relația dintre variabile relevante din domeniu (distanța de livrare, timpul de preparare, nivelul traficului, condițiile meteo, momentul zilei și experiența curierului) și timpul final de livrare.

Procesul de generare a fost realizat folosind distribuții controlate și reguli inspirate din scenarii reale de livrare (de exemplu, creșterea timpului de livrare în condiții de trafic intens sau vreme nefavorabilă, influența experienței curierului asupra eficienței livrării). Pentru a evita date triviale sau deterministe, a fost introdus zgomot aleator controlat, astfel încât datele generate să prezinte variabilitate realistă, dar să păstreze coerența fizică și logică a procesului simulat.

În urma acestui proces, au fost generate 10.000 de observații originale, care au fost combinate cu cele 1.000 de observații din datasetul public, rezultând un set final de 11.000 de observații, din care 90.9% reprezintă contribuție originală. Preprocesarea a fost refăcută integral pe datasetul combinat, conform cerințelor proiectului, iar aceste date au fost ulterior utilizate pentru antrenarea și evaluarea rețelei neuronale, demonstrând capacitatea sistemului de a generaliza și de a produce predicții realiste ale timpului de livrare.


**Locația codului:** `src/data_acquisition/generate.py`
**Locația datelor:** `data/generated/` 

**Dovezi:**
- Grafic comparativ: `docs/generated_vs_real.png`
- Setup experimental: `docs/acquisition_setup.jpg` (dacă aplicabil)
- Tabel statistici: `docs/data_statistics.csv`
```
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

**Notă pentru proiecte simple:**
Chiar dacă aplicația voastră este o clasificare simplă (user upload → classify → display), trebuie să modelați fluxul ca un State Machine. Acest exercițiu vă învață să gândiți modular și să anticipați toate stările posibile (inclusiv erori).

**Legendă obligatorie (scrieți în README):**
```markdown

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


