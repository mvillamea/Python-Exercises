"""Crear un programa que pida al usuario su edad y muestra por pantalla
si es mayor de edad o no, siendo 18 años la mayoría de edad."""

edad = input("Ingrese su edad: ")

edad = int(edad)

def mayor_edad(edad):
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")

print(mayor_edad(edad))