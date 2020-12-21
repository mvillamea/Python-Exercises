"""Crear un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
precio
de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un
mensaje informando de ello.
Fruta Precio (kg)
Banana 80
Manzana 100
Pera 50
Naranja 70"""

precios_frutas = {
    "Fruta_1": {"Fruta": "Banana",
              "Precio": 80},
    "Fruta_2": {"Fruta": "Manzana",
               "Precio": 100},
    "Fruta_3": {"Fruta": "Pera",
               "Precio": 50},
    "Fruta_4": {"Fruta": "Naranja",
               "Precio": 70},
}

fruta = input("¿Qué fruta desea? ")

kilos = float(input("Ingrese la cantidad de kilos deseada: "))

if fruta == precios_frutas["Fruta_1"]["Fruta"]:
    precio = int(precios_frutas["Fruta_1"]["Precio"])*kilos
    print("El precio es ", precio,"." )
elif fruta == precios_frutas["Fruta_2"]["Fruta"]:
    precio = int(precios_frutas["Fruta_2"]["Precio"])*kilos
    print("El precio es ", precio,"." )
elif fruta == precios_frutas["Fruta_3"]["Fruta"]:
    precio = int(precios_frutas["Fruta_3"]["Precio"]) * kilos
    print("El precio es ", precio, ".")
elif fruta == precios_frutas["Fruta_4"]["Fruta"]:
    precio = int(precios_frutas["Fruta_4"]["Precio"]) * kilos
    print("El precio es ", precio, ".")
else:
    print("La fruta no está en la lista de precios.")

