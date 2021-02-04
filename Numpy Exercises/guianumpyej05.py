"""Crear una matriz identidad de 6x6."""

import numpy as np

# Forma 1

identidad = np.eye(6)

# Forma 2

def vector_identidad(n, m):
    lista = []
    for i in range(m):
        if i != n:
            lista += [0]
        else:
            lista += [1]
    return tuple(lista)

def matriz_identidad(m):
    lista = []
    for i in range(m):
        lista += [vector_identidad(i, m)]
    return np.array(lista)



