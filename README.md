# Retele-Neuronale
Proiect Retele Neuronale
# 📘 README – Etapa 3: Analiza și Pregătirea Setului de Date pentru Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** [Belu Maria Alexandra]  
**Data:** [25.10.2025]  

---

## Introducere

Acest document descrie activitățile realizate în **Etapa 3**, în care se analizează și se preprocesează setul de date necesar proiectului „Rețele Neuronale". Scopul etapei este pregătirea corectă a datelor pentru instruirea modelului RN, respectând bunele practici privind calitatea, consistența și reproductibilitatea datelor.

---

##  1. Structura Repository-ului Github (versiunea Etapei 3)

```
project-name/
├── README.md
├── docs/
│   └── datasets/          # descriere seturi de date, surse, diagrame
├── data/
│   ├── raw/               # date brute
│   ├── processed/         # date curățate și transformate
│   ├── train/             # set de instruire
│   ├── validation/        # set de validare
│   └── test/              # set de testare
├── src/
│   ├── preprocessing/     # funcții pentru preprocesare
│   ├── data_acquisition/  # generare / achiziție date (dacă există)
│   └── neural_network/    # implementarea RN (în etapa următoare)
├── config/                # fișiere de configurare
└── requirements.txt       # dependențe Python (dacă aplicabil)
```

---

##  2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** Dataset public disponibil pe platforma Kaggle, titlul: “Food Delivery Time Prediction”, creat de utilizatorul Den Kuznetz.
* **Link sursă:** https://www.kaggle.com/datasets/denkuznetz/food-delivery-time-prediction
* **Modul de achiziție:** Fișier CSV descărcat manual din Kaggle și importat în proiect.
* **Perioada / condițiile colectării:** Set de date sintetic, generat pe baza unor scenarii realiste din domeniul livrării comenzilor de mâncare, incluzând informații despre distanță, trafic, meteo, vehicul și experiența curierului.

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** 1000
* **Număr de caracteristici (features):** 9-> 8 features + 1 target
* **Tipuri de date:**  Numerice, Categoriale 
* **Format fișiere:** CSV 

### 2.3 Descrierea fiecărei caracteristici

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


**Fișier recomandat:**  `data/README.md`

---

##  3. Analiza Exploratorie a Datelor (EDA) – Sintetic

### 3.1 Statistici descriptive aplicate

* **Medie, mediană, deviație standard**
* **Min–max și quartile**
* **Distribuții pe caracteristici** (histograme)
* **Identificarea outlierilor** (IQR / percentile)

### 3.2 Analiza calității datelor

* **Detectarea valorilor lipsă** (% pe coloană)
* **Detectarea valorilor inconsistente sau eronate**
* **Identificarea caracteristicilor redundante sau puternic corelate**

### 3.3 Probleme identificate

* [exemplu] Feature X are 8% valori lipsă
* [exemplu] Distribuția feature Y este puternic neuniformă
* [exemplu] Variabilitate ridicată în clase (class imbalance)

---

##  4. Preprocesarea Datelor

### 4.1 Curățarea datelor

* **Eliminare duplicatelor**
* **Tratarea valorilor lipsă:**
  * Feature A: imputare cu mediană
  * Feature B: eliminare (30% valori lipsă)
* **Tratarea outlierilor:** IQR / limitare percentile

### 4.2 Transformarea caracteristicilor

* **Normalizare:** Min–Max / Standardizare
* **Encoding pentru variabile categoriale**
* **Ajustarea dezechilibrului de clasă** (dacă este cazul)

### 4.3 Structurarea seturilor de date

**Împărțire recomandată:**
* 70–80% – train
* 10–15% – validation
* 10–15% – test

**Principii respectate:**
* Stratificare pentru clasificare
* Fără scurgere de informație (data leakage)
* Statistici calculate DOAR pe train și aplicate pe celelalte seturi

### 4.4 Salvarea rezultatelor preprocesării

* Date preprocesate în `data/processed/`
* Seturi train/val/test în foldere dedicate
* Parametrii de preprocesare în `config/preprocessing_config.*` (opțional)

---

##  5. Fișiere Generate în Această Etapă

* `data/raw/` – date brute
* `data/processed/` – date curățate & transformate
* `data/train/`, `data/validation/`, `data/test/` – seturi finale
* `src/preprocessing/` – codul de preprocesare
* `data/README.md` – descrierea dataset-ului

---

##  6. Stare Etapă (de completat de student)

- [ ] Structură repository configurată
- [ ] Dataset analizat (EDA realizată)
- [ ] Date preprocesate
- [ ] Seturi train/val/test generate
- [ ] Documentație actualizată în README + `data/README.md`

---
