"""Crear un programa que muestre el eco de todo lo que le usuarie introduzca hasta que
le usuarie escriba “salir” que terminará."""


def eco ():
    ingreso_inicial = input("Ingrese algo: ")

    print(ingreso_inicial)

    otro_ingreso = input("Ingrese otra cosa: ")

    while otro_ingreso != "salir":
        print (otro_ingreso)
        otro_ingreso = input("Ingrese otra cosa: ")

eco()




