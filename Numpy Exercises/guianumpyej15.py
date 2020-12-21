"""Crear una matriz que contenga información en distintos formatos, imprimir la info
de cada formato a través del atributo."""

import numpy as np

data_2 = np.rec.array([('Alice', 25, 1.55), ('Bob', 35, 1.81), ('Cathy', 45, 1.67), ('Doug', 55, 1.78)],
                      dtype = [('name', 'U10'), ('age','i4'), ('height', 'f8')])

print(data_2)
print(data_2.name)
print(data_2.age)
print(data_2.height)