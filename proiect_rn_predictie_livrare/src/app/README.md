# UI/Web Service (Etapa 4)

Aplicație Streamlit care primește input de la utilizator și produce o predicție (demo).

## Rulare
```bash
python -m streamlit run src/app/app_final.py

Regenerarea Datelor 

python -m src.data_acquisition.generate
python -m src.preprocessing.combine_datasets
python -m src.preprocessing.data_cleaner
python -m src.preprocessing.feature_engineering
python -m src.preprocessing.data_splitter

Crearea Scaler-ului

python -m src.preprocessing.fit_preprocessing_pipeline


Antrenarea Modelului

python -m src.neural_network.train


Generarea Rapoartelor

python -m src.docs.confusion_matrix_optimized
python -m src.docs.plot_loss_curve
