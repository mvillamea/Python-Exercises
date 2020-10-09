"""Crear un programa que pregunte el nombre del usuario y un número entero e imprima
por pantalla en líneas distintas el nombre del usuario tantas veces como el número
introducido."""

nombre = input("Nombre: ")
numero = input("Elija un número entero: ")

i = 0
while i < int(numero):
    print(nombre)
    i = i + 1
