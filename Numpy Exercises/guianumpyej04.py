"""Encontrar los índices que no son ceros del arreglo
[1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]."""

import numpy as np

array = np.array([1, 2, 4, 2, 4, 0, 1, 0, 0, 0, 12, 4, 5, 6, 7, 0])

print(np.where(array != 0 ))

