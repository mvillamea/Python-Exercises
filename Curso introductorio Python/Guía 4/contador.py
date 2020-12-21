
def cambio_contador(argumento):
    """La siguiente función recibe
    un argumento y a ese argumento
    lo incrementa en 1 si le usuarie ingresa inc,
    lo decrementa en 1 si le usuarie ingresa dec,
    lo deja igual si el usuarie no ingresa nada
    o el ingreso no es válido"""
    ingreso=input('Ingrese lo que desee hacer con el contador: ')
    if ingreso == 'inc':
        argumento+=1
        print("Se ha actualizado el contador a", argumento)
    elif ingreso == 'dec':
        argumento-=1
        print("Se ha actualizado el contador a", argumento)
    elif ingreso == "":
        argumento=argumento
    else:
        print("El ingreso no es válido.")
    return str(argumento)


try:
    with open("contador.txt", "a+") as contador:
        contador.seek(0)
        cont = contador.read()
        print("El contador está en", cont)
        global cambio
        cambio = cambio_contador(int(cont)) #calculamos el nuevo valor
        contador.write(cambio) #guardamos el nuevo valor en el archivo
        contador.close()
    #ahora vamos a guardar solo el nuevo valor en el archivo
    with open ("contador.txt", "w+") as contador1:
        contador1.write(cambio)
        contador1.close()

except FileNotFoundError:
    #Si el achivo no existe, lo creamos con 0 en su contenido
    with open("contador.txt", "w+") as contador:
        contador.write('0')
        contador.close()


