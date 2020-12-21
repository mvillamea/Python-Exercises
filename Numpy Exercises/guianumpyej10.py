""".Crear una matriz de 20x20 de valores aleatorios entre 1 y 100, luego indicar su
media, su mediana, su moda y el desvío estándar. Los valores que den como
resultado flotantes deben tener como máximo 2 decimales."""

import numpy as np

from scipy import stats

np.random.seed(0)

matriz = np.random.randint(1, 101, (20, 20))

print(matriz)

media = round(np.mean(matriz), 2)

mediana = round(np.median(matriz), 2)

moda = stats.mode(matriz)

sd = round(np.std(matriz), 2)

print('La media es', media)
print('La mediana es', mediana)
print('La moda es', moda)
print('El desvío estándar es', sd)

