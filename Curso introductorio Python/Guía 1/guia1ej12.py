"""Crear un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero, el programa debe devolver un mensaje indicando que no se puede
dividir por 0."""

def dividir ():
    num_1 = input("Ingrese un número: ")
    num_1 = int(num_1)

    num_2 = input("Ingrese otro número: ")
    num_2 = int(num_2)

    if num_2 == 0:
        print("No se puede dividir por cero")
    else:
        print(num_1/num_2)
