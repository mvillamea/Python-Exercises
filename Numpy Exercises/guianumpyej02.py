"""Invertir el vector creado en el ejercicio 1:
Crear un vector con valores dentro del rango 10 a 49."""

import numpy as np

#Forma 1

lista = range(49, 9, -1)

arreglo = np.array(lista)

print(arreglo)

#Forma 2

lista_2 = range(10, 50, 1)

arreglo_2 = np.array(lista_2)

print(arreglo_2[::-1])