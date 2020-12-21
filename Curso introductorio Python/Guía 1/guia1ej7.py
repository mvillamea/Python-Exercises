"""Crear un programa que pida al usuario dos números enteros y muestre por pantalla la
<n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera
respectivamente."""

numero_1 = input("Elija un número entero: ")

numero_2 = input("Elija otro número entero: ")

numero_1 = int(numero_1)

numero_2 = int(numero_2)

cociente = numero_1 // numero_2

resto = numero_1 % numero_2

print("La división entre ", numero_1, " y ", numero_2, "da como cociente ", cociente, " y como resto ", resto)
