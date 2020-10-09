"""Crear un programa que pregunte al usuario su
edad y muestre por pantalla todos los
años que ha cumplido (desde 1 hasta su edad)."""

edad_ingresada = int(input("Ingrese su edad: "))

def imprime_edades_pasadas (edad):
    i = 1
    while i <= edad:
        print(i)
        i +=1

imprime_edades_pasadas(edad_ingresada)