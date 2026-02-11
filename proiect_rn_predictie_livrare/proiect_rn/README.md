# Overview General al Proiectului

Acest proiect are ca obiectiv dezvoltarea unui **Sistem Inteligent Artificial (SIA)** pentru predicția timpului de livrare a comenzilor de mâncare, utilizând tehnici de învățare automată și rețele neuronale artificiale. 

Sistemul este conceput pentru a sprijini deciziile operaționale din cadrul unei platforme de livrare, oferind:
* O estimare numerică precisă a timpului de livrare (în minute);
* O clasificare a comenzii în funcție de rapiditatea livrării (fast / medium / slow).

---

### Problematica
Problema abordată este una relevantă din punct de vedere industrial, deoarece predicțiile inexacte ale timpului de livrare pot conduce la nemulțumirea clienților, încălcarea acordurilor de nivel de serviciu (SLA) și ineficiență operațională. Prin urmare, proiectul urmărește nu doar obținerea unei acurateți ridicate, ci și înțelegerea erorilor, impactul lor asupra aplicației reale și propunerea de măsuri corective.

### Datele Utilizate
Datele utilizate provin dintr-un dataset public combinat cu date generate artificial, astfel încât contribuția originală să depășească pragul de 40%. Setul de date include caracteristici relevante precum:
* Distanța de livrare;
* Condițiile meteo;
* Nivelul de trafic;
* Momentul zilei;
* Tipul vehiculului;
* Timpul de preparare;
* Experiența curierului.

Datele sunt preprocesate riguros prin curățare, inginerie de caracteristici și transformări consistente între faza de antrenare și inferență.

### Arhitectura Modelului
Modelul central al sistemului este o rețea neuronală de tip **MLP (Multi-Layer Perceptron) multitask**, care utilizează un trunchi comun de straturi ascunse și două capete de ieșire: 
1.  **Regresie**: predicția timpului de livrare;
2.  **Clasificare**: rapiditatea livrării. 

Această arhitectură permite exploatarea relațiilor comune dintre sarcini și îmbunătățește generalizarea modelului.

### Procesul de Antrenare și Evaluare
Procesul de antrenare este controlat prin hiperparametri documentați explicit, utilizând optimizatorul **Adam**, mecanisme de **EarlyStopping**, **ReduceLROnPlateau** și **ModelCheckpoint**, iar performanța este evaluată pe un set de test separat, folosind metrici adecvate atât pentru regresie (**MAE, RMSE**), cât și pentru clasificare (**Accuracy, F1-score macro**). Rezultatele obținute demonstrează o bună capacitate de generalizare și o predicție precisă a timpului de livrare.

### Implementare Practică
În final, proiectul include o aplicație web interactivă care permite introducerea parametrilor unei comenzi și afișarea predicției în timp real, simulând un scenariu de utilizare industrială. Prin analiza erorilor, matricea de confuzie și măsurile corective propuse, proiectul demonstrează o abordare completă, de la date și modelare, până la evaluare și integrare practică.