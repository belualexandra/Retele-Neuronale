### Justificare pentru arhitectura aleasă

Am ales o arhitectură de tip MLP (Multi-Layer Perceptron) pentru că problema noastră este una de date tabulare (feature-uri numerice și categorice) și nu implică imagini sau secvențe temporale. În acest context, un MLP este o alegere standard și eficientă deoarece poate învăța relații neliniare între variabile precum distanța, timpul de preparare, traficul, vremea, momentul zilei și experiența curierului, fără a necesita structuri speciale (ex. CNN/RNN) care sunt dedicate altor tipuri de date.


### Modelul  are două obiective complementare:

Regresie: predicția timpului de livrare în minute (Delivery_Time_min)

Clasificare: încadrarea comenzii într-o clasă (Delivery_Class: fast/medium/slow)

Am ales un model multitask (un “trunchi” comun + două capete de ieșire) pentru că cele două sarcini folosesc aceleași informații de intrare și sunt corelate: dacă o comandă este „slow”, de regulă timpul estimat în minute este mai mare. Prin învățarea comună a reprezentării interne, modelul poate extrage mai bine tipare generale (ex. trafic + vreme + distanță → întârziere) și apoi să le folosească atât pentru regresie, cât și pentru clasificare. În plus, această abordare reduce duplicarea (nu antrenăm două modele complet separate) și este mai ușor de integrat în aplicația web.


În straturile ascunse folosim ReLU, deoarece este eficientă pentru antrenare, introduce neliniaritate și reduce riscul de „vanishing gradients” comparativ cu activări precum sigmoid/tanh.

Pentru ieșirea de regresie folosim activare lineară, deoarece timpul estimat este o valoare continuă.

Pentru ieșirea de clasificare folosim Softmax, deoarece întoarce probabilități pe cele 3 clase, ușor de interpretat și corect pentru clasificare multi-clasă.



### Arhitectura MLP (date tabulare) este ușor de folosit în producție deoarece:

input-ul este un vector numeric rezultat din pipeline-ul de preprocesare (scaler + one-hot);

modelul are dimensiune mică/medie și predicția este rapidă;

folosind același pipeline salvat și încărcat la inferență, se evită erorile de tip „train/inference mismatch” (care pot duce la predicții foarte greșite).

### Concluzie

Arhitectura aleasă (MLP multitask) este justificată prin:

potrivirea cu natura datelor (tabulare);

capacitatea de a modela relații neliniare;

posibilitatea de a produce simultan o predicție numerică (minute) și una categorială (clasă);

integrarea simplă și stabilă în aplicația web, folosind același pipeline de preprocesare ca în antrenare.