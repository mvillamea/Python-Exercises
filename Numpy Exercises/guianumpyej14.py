""".Crear un arreglo de 4 elementos de entre 0 y 10, informar la cantidad de
elementos que tiene y también cuántos bytes ocupa el arreglo."""

import numpy as np

np.random.seed(0)

array = np.random.randint(0, 11, 4)

print('La cantidad de elementos del array es:', array.size)

print('La cantidad de bytes que ocupa el array es:', array.itemsize)

