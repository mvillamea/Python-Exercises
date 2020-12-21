"""Encontrar los índices de los valores mínimos y máximos
de la matriz creada en el ejercicio 3."""

import numpy as np

# Lugares mínimos y máximos primera matriz

matriz_1 = np.array(([0, 1, 2], [3, 4, 5], [6, 7, 8]))

minimo_1 = matriz_1.min()

ind_min_1 = np.where(matriz_1 == minimo_1 )

print(ind_min_1)

maximo_1 = matriz_1.max()

ind_max_1 = np.where(matriz_1 == maximo_1)

print(ind_max_1)

# Lugares mínimos y máximos segunda matriz

np.random.seed(0)

matriz_2 = np.random.randint(0, 9, (3, 3))

minimo_2 = matriz_2.min()

ind_min_2 = np.where(matriz_2 == minimo_2 )

print(ind_min_2)

maximo_2 = matriz_2.max()

ind_max_2 = np.where(matriz_2 == maximo_2)

print(ind_max_2)



