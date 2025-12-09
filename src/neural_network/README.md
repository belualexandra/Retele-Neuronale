# Modul 2 – Neural Network (Arhitectura SIA)

Acest modul implementează scheletul rețelei neuronale utilizate pentru problema de predicție
a timpului de livrare al comenzilor de mâncare. În această etapă (Etapa 4) modelul nu este încă
antrenat complet; se construiește doar arhitectura de bază și se verifică funcționarea
pipeline-ului SIA.


## 1. Arhitectura rețelei neuronale

Modelul utilizat este un Multi-Layer Perceptron (MLP) cu straturi complet conectate.
Arhitectura este următoarea:

- **Input Layer:** dimensiune = numărul de features rezultate după preprocesare
- **Dense Layer 1:** 64 neuroni, activare ReLU
- **Dense Layer 2:** 32 neuroni, activare ReLU
- **Output Layer:** 1 neuron, ieșire pentru regresie (timp de livrare, în minute)

Funcția de pierdere (loss): `MSE`  
Optimizator: `Adam`  
Metrică monitorizată: `MAE`

Această arhitectură este potrivită pentru date tabulare și relații neliniare între variabile
(distanță, trafic, meteo, tip vehicul etc.), fiind un model standard în probleme de regresie.


## 2. Implementare

Codul arhitecturii se află în:src/neural_network/model.py


Acesta conține funcția `build_model(input_dim)` care:

- construiește straturile rețelei
- compilează modelul
- returnează o instanță Keras pregătită pentru antrenare


## 3. Inițierea procesului de antrenare (schelet)

Fișierul: src/neural_network/train.py

realizează următoarele:

1. Încarcă datele preprocesate din Etapa 3 (`data/processed/`)
2. Construiește rețeaua neuronală prin `build_model()`
3. Afișează arhitectura completă a modelului (summary)
4. Confirmă că modelul este pregătit pentru antrenare în Etapa 5

Exemplu de output generat:

Arhitectura rețelei:
Layer (type) Output Shape Param #

Dense (64) (None, 64) 1408
Dense (32) (None, 32) 2080
Dense (1) (None, 1) 33
Total params: 3521
Modelul este pregătit pentru antrenare.


---

## 4. Motivația alegerii arhitecturii

- Datele problemei sunt **tabulare**, nu imagini sau text  
- Relațiile între variabile sunt **neliniare**, deci sunt necesare straturi Dense cu ReLU  
- Modelul este suficient de simplu pentru a evita supraînvățarea, dar suficient de puternic
  pentru a învăța dependențe complexe între distanță, trafic, meteo, vehicul și timpul final
  de livrare
- ReLU și Adam sunt standard în probleme de regresie și oferă stabilitate și viteză bună de convergență

Aceasta este versiunea inițială a modelului; îmbunătățiri (dropout, batch normalization,
ajustare hiperparametri) pot fi introduse în Etapa 5.

---

## 5. Cum se rulează modulul

Din directorul principal al proiectului: python src/neural_network/train.py


Acest script verifică faptul că modelul poate fi construit corect și că datele preprocesate
pot fi încărcate fără erori.

---

## 6. Status Etapă

- [x] Arhitectură RN definită și documentată
- [x] Cod complet `model.py`
- [x] Cod schelet `train.py`
- [x] README actualizat
- [x] Arhitectură testată cu succes prin `model.summary()`





