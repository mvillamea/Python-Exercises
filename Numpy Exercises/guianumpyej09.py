"""Crear dos arreglos al azar A y B, verificar si son iguales"""

import numpy as np

np.random.seed(0)

array1 = np.random.random(4)

array2 = np.random.random(4)

print(id(array1)==id(array2))

