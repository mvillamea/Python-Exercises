"""Crear una matriz de 3x3 con los valores de 0 a 8."""

import numpy as np

# Forma 1

matriz_1 = np.array(([0, 1, 2], [3, 4, 5], [6, 7, 8]))

print(matriz_1)


# Forma 2
np.random.seed(0)

matriz_2 = np.random.randint(0, 9, (3, 3))

print(matriz_2)