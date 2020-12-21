"""Crear dos arreglos de 4 elementos enteros y hacer las siguientes operaciones:
sumarlos, restarle el segundo al primero, multiplicarlos, dividir el primero por el
segundo. Hacerlo utilizando métodos."""

import numpy as np

np.random.seed(0)

array1 = np.random.randint(0, 100, 4, dtype=np.int64)

print('Primer arreglo:', array1)

array2 = np.random.randint(0, 100, 4, dtype=np.int64)

print ('Segundo arreglo:', array2)

print('La suma es:', np.add(array1, array2))

print('La resta es:', np.subtract(array1, array2))

print('La multiplicación es:', np.multiply(array1, array2))

print('La división es:', np.divide(array1, array2))



