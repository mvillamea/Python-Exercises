"""Crear un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión."""

capital_inicial = input("Ingrese la cantidad a invertir: ")

capital_inicial = int(capital_inicial)

interes_anual = input("Ingrese el interés anual de la inversión: ")

interes_anual = float(interes_anual)

cantidad_years = input("Ingrese la cantidad de años que va a invertir: ")

cantidad_years = int(cantidad_years)

interes_simple = capital_inicial * (1 + interes_anual*cantidad_years)

print(interes_simple)

