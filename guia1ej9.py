"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
hacer venta por correo y la empresa de logística les cobra por el peso de cada paquete
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a
demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Crear un programa que lea
el número de payasos y muñecas vendidos en el último pedido y calcule el peso total
del paquete que será enviado. Mostrar el resultado por pantalla."""


munecas = input("Ingrese la cantidad de muñecas del pedido: ")
munecas = int(munecas)

payasos = input("Ingrese la cantidad de payasos del pedido: ")
payasos = int(payasos)

peso = 112*payasos + 75*munecas

print("El peso total del paquete a enviar es", peso)