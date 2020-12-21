"""Crear dos arreglos de 6 elementos de valores aleatorios entre 0 y 1 y luego
realizar las operaciones lógicas and y or con los métodos de NumPy"""

import numpy as np

np.random.seed(0)

array1 = np.random.randint(0, 2, 6)

array2 = np.random.randint(0, 2, 6)

print('Primer arreglo:', array1)

print('Segundo arreglo:', array2)

print('And:', array1 & array2)

print('Or:', array1 | array2)