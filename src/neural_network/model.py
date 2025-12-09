"""
model.py – Arhitectura Rețelei Neuronale
---------------------------------------

Acest modul definește arhitectura rețelei neuronale utilizate pentru
predicția timpului de livrare al comenzilor de mâncare.

Rețeaua este de tip Multi-Layer Perceptron (MLP) și funcționează pe date
preprocesate (numeric scalate și categorice one-hot-encoded).

Input shape = numărul de features rezultate după preprocesare.
Output = timp de livrare (regresie).

Straturi folosite:
- Dense(64) + ReLU
- Dense(32) + ReLU
- Dense(1)  – ieșirea rețelei
"""

import tensorflow as tf
from tensorflow.keras import layers, models


def build_model(input_dim: int):
    """
    Construiește și returnează un model MLP pentru regresie.

    Parametri:
        input_dim (int): numărul de features de intrare după preprocesare.

    Return:
        model (tf.keras.Model): modelul compilat.
    """
    model = models.Sequential([
        layers.Input(shape=(input_dim,)),

        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),

        layers.Dense(1)  # ieșire pentru regresie
    ])

    model.compile(
        optimizer="adam",
        loss="mse",
        metrics=["mae"]
    )

    return model
