"""Crear un programa que almacene la cadena de caracteres  contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable."""

def es_igual ():
    password = "contraseña"

    password_user = input("Ingrese la contraseña: ")

    if password_user == password:
        print("La constraseña introducida coincide con la guardada")
    else:
        print("La constraseña introducida no coincide con la guardada")