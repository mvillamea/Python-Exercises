"""Crear un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase."""


frase_ingresada = input("Ingrese una frase: ")

letra_ingresada = input("Ingrese una letra: ")

#Devuelve la cantidad de veces que está la letra en la palabra
print(frase_ingresada.count(letra_ingresada))
