"""Crear un programa que pida al usuario un número entero y muestre por pantalla si es
par o impar."""

def par_o_impar ():
    num = input("Ingrese un número: ")
    num = int(num)

    if num % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

par_o_impar()