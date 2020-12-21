"""Crear un programa que pida al usuario una palabra y luego muestre por pantalla una a
una las letras de la palabra introducida empezando por la última."""


palabra_ingresada = input("Ingrese una palabra: ")

def imprime_letras_reversa (palabra):
    """Imprime las letras de una
       palabra dada de atrás hacia adelante"""
    i = len(palabra)
    while i > 0:
        print(palabra[i-1])
        i = i-1

imprime_letras_reversa(palabra_ingresada)

