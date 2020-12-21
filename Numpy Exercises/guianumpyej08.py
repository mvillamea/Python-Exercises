"""Crear una matriz de 5x5 con valores en los renglones que vayan de 0 a 4."""

import numpy as np

np.random.seed(0)

matriz = np.random.randint(0, 5, (5, 5))

print(matriz)