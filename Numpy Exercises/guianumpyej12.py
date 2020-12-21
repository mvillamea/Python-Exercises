"""Crear una matriz de 4x4 de valores aleatorios entre 1 y 10, y luego agregarle
una fila de 0s al final."""

import numpy as np

np.random.seed(0)

matriz = np.random.randint(1, 11, (4, 4))

matriz = np.append(matriz, [[0, 0, 0, 0]], axis=0)

print(matriz)