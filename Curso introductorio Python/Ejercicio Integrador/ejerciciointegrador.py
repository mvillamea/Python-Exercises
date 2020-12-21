"""Crear un programa que sea un controlador de gastos mensuales, que podamos ingresar
gastos e ingresos mes a mes y nos vaya actualizando la información.
Puede ser con POO, programación funcional o estructurada, y se le pueden agregar GUIs."""

import pandas as pd

#creamos el excel file
"""fecha = []

venta = []

publicidad = []

data = { }

df = pd.DataFrame(data, columns = [])

df.to_excel('gastos.xlsx', sheet_name='gastos')"""


def agrego_gastos():
    excel = pd.read_excel('gastos.xlsx', index_col=0)
    ingreso_1 = input('¿Desea ingresar un nuevo gasto? ')
    while ingreso_1 == 'si':
        nombre_nuevo = input('Ingrese el nombre del gasto: ')
        valor_nuevo = input('Ingrese el valor del gasto: ')
        fecha_nueva = input('Ingrese la fecha del gasto: ')
        excel = excel.append(
            {'Nombre': nombre_nuevo,
             'Valor': valor_nuevo,
             'Fecha': fecha_nueva},
            ignore_index=True
            )
        ingreso_1 = input('¿Desea ingresar un nuevo gasto? ')
    excel.to_excel("gastos.xlsx")
    print(excel)

agrego_gastos()









