"""Crear una matriz de 10x10 con 1 en los bordes
y 0 en el interior (con rangos de índices)."""

import numpy as np

unos = np.ones((10, 10), dtype=np.int64)

ceros = np.zeros((10, 10), dtype=np.int64)

fila_unos = unos[0:1, 1:9]

fila_ceros = ceros[0:1, 1:9]

columna_unos = unos[0:10, 0:1]

matriz = np.append(fila_unos, fila_ceros, axis=0)

matriz = np.append(matriz, fila_ceros, axis=0)

matriz = np.append(matriz, fila_ceros, axis=0)

matriz = np.append(matriz, fila_ceros, axis=0)

matriz = np.append(matriz, fila_ceros, axis=0)

matriz = np.append(matriz, fila_ceros, axis=0)

matriz = np.append(matriz, fila_ceros, axis=0)

matriz = np.append(matriz, fila_ceros, axis=0)

matriz = np.append(matriz, fila_unos, axis=0)

matriz = np.append(matriz, columna_unos, axis=1)

matriz = np.append(columna_unos, matriz, axis=1)

print(matriz)

print(matriz.shape)









