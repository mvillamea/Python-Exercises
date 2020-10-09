tablero_tateti = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

def imprimir_tablero(tablero):  # imprime el tablero
    for row in tablero:
        print("|", row[0], "|", row[1], "|", row[2], "|", sep='')


def chequeo_casillero(tablero, fila, columna):
    if int(fila) not in {1, 2, 3}:
        """chequea que la fila dada esté dentro
           de la cantidad de filas del tablero"""
        print("La fila elegida no es válida")
        fila = int(input("Elija una fila para ubicar su letra: "))

    elif int(columna) not in {1, 2, 3}:
        """chequea que la columna dada esté dentro  
           de la cantidad de columnas del tablero"""
        print("La columna elegida no es válida")
        columna = int(input("Elija una columna para ubicar su letra: "))

    elif tablero[int(fila) - 1][int(columna) - 1] == 'X':
        # chequea que el casillero no esté ocupado por una X
        print("El casillero elegido está ocupado")
        fila = int(input("Elija una fila para ubicar su letra: "))
        columna = int(input("Elija una columna para ubicar su letra: "))

    elif tablero[int(fila) - 1][int(columna) - 1] == 'O':
        # chequea que el casillero no esté ocupado por una O
        print("El casillero elegido está ocupado")
        fila = int(input("Elija una fila para ubicar su letra: "))
        columna = int(input("Elija una columna para ubicar su letra: "))

    else:
        fila = fila
        columna = columna

    return [fila, columna]



def pongo_letra(fila, columna, tablero, letra):
    """La función pongo ubica la opción
       elegida en el casillero dado del tablero"""
    tablero[int(fila) - 1][int(columna) - 1] = letra

#La función chequeo_termina comprueba si el juego terminó y cómo o si no terminó
def chequeo_termina(tablero):
    resultado = 5
    if tablero[1][1] == 'X' and tablero[1][2] == 'X' and tablero[1][0] == 'X':
        # chequea si la 2da fila es toda x y en ese caso que termine
        resultado = 6
        print("¡El juego ha terminado! Ganó X")
    elif tablero[1][1] == 'O' and tablero[1][2] == 'O' and tablero[1][0] == 'O':
        # chequea si la 2da fila es toda O
        resultado = 6
        print("¡El juego ha terminado! Ganó O")
    elif tablero[2][1] == 'X' and tablero[2][2] == 'X' and tablero[2][0] == 'X':
        # chequea si la 3ra fila es toda X
        resultado = 6
        print("¡El juego ha terminado! Ganó X")
    elif tablero[2][1] == 'O' and tablero[2][2] == 'O' and tablero[2][0] == 'O':
        # chequea si la 3ra fila es toda O
        resultado = 6
        print("¡El juego ha terminado! Ganó O")
    elif tablero[0][1] == 'X' and tablero[0][2] == 'X' and tablero[0][0] == 'X':
        # chequea si la 1ra fila es toda X
        resultado = 6
        print("¡El juego ha terminado! Ganó X")
    elif tablero[0][1] == 'O' and tablero[0][2] == 'O' and tablero[0][0] == 'O':
        # chequea si la 1ra fila es toda O
        resultado = 6
        print("¡El juego ha terminado! Ganó O")
    elif tablero[1][1] == 'X' and tablero[2][1] == 'X' and tablero[0][1] == 'X':
        # chequea si la 2da columna es toda X
        resultado = 6
        print("¡El juego ha terminado! Ganó X")
    elif tablero[1][1] == 'O' and tablero[2][1] == 'O' and tablero[0][1] == 'O':
        # chequea si la 2da columna es toda O
        resultado = 6
        print("¡El juego ha terminado! Ganó O")
    elif tablero[1][2] == 'X' and tablero[2][2] == 'X' and tablero[0][2] == 'X':
        # chequea si la 3ra columna es toda X
        resultado = 6
        print("¡El juego ha terminado! Ganó X")
    elif tablero[1][2] == 'O' and tablero[2][2] == 'O' and tablero[0][2] == 'O':
        # chequea si la 3ra columna es toda O
        resultado = 6
        print("¡El juego ha terminado! Ganó O")
    elif tablero[1][0] == 'X' and tablero[2][0] == 'X' and tablero[0][0] == 'X':
        # chequea si la 1ra columna es toda X
        resultado = 6
        print("¡El juego ha terminado! Ganó X")
    elif tablero[1][0] == 'O' and tablero[2][0] == 'O' and tablero[0][0] == 'O':
        # chequea si la 1ra columna es toda O
        resultado = 6
        print("¡El juego ha terminado! Ganó O")
    elif tablero[1][1] == 'X' and tablero[2][2] == 'X' and tablero[0][0] == 'X':
        # chequea si la diagonal decreciente es toda X
        resultado = 6
        print("¡El juego ha terminado! Ganó X")
    elif tablero[1][1] == 'O' and tablero[2][2] == 'O' and tablero[0][0] == 'O':
        # chequea si la diagonal decreciente es toda O
        resultado = 6
        print("¡El juego ha terminado! Ganó O")
    elif tablero[2][0] == 'X' and tablero[1][1] == 'X' and tablero[0][2] == 'X':
        # chequea si la diagonal creciente es toda X
        resultado = 6
        print("¡El juego ha terminado! Ganó X")
    elif tablero[2][0] == 'O' and tablero[1][1] == 'O' and tablero[0][2] == 'O':
        # chequea si la diagonal creciente es toda O
        resultado = 6
        print("¡El juego ha terminado! Ganó O")
    elif (tablero[1][1] in {'X', 'O'}) and (tablero[1][2] in {'X', 'O'}) and (tablero[1][0] in {'X', 'O'}) and (
            tablero[2][1] in {'X', 'O'}) and (tablero[2][2] in {'X', 'O'}) and (tablero[2][0] in {'X', 'O'}) and (
            tablero[0][1] in {'X', 'O'}) and (tablero[0][2] in {'X', 'O'}) and (tablero[0][0] in {'X', 'O'}):
        # chequea si el tablero está lleno sin que nadie gane
        resultado = 6
        print("¡El juego ha terminado! Es un empate")
    else:
        resultado = resultado

    return resultado



"""imprimir_tablero(tablero_tateti)
fila_casillero = int(input("Elija una fila para ubicar su letra: "))
columna_casillero = int(input("Elija una columna para ubicar su letra: "))
chequeo_casillero(tablero_tateti, fila_casillero, columna_casillero)
print(chequeo_casillero(tablero_tateti, fila_casillero, columna_casillero))
pongo_letra(chequeo_casillero(tablero_tateti, fila_casillero, columna_casillero)[0], chequeo_casillero(tablero_tateti, fila_casillero, columna_casillero)[1], tablero_tateti, 'X')
imprimir_tablero(tablero_tateti)"""

i = 0
for i in range(9):
    imprimir_tablero(tablero_tateti)
    fila_casillero = int(input("Elija una fila para ubicar su letra: "))
    columna_casillero = int(input("Elija una columna para ubicar su letra: "))
    chequeo_casillero(tablero_tateti, fila_casillero, columna_casillero)
    """print(chequeo_casillero(tablero_tateti, fila_casillero, columna_casillero))"""
    if i%2 == 0:
        pongo_letra(chequeo_casillero(tablero_tateti, fila_casillero, columna_casillero)[0],
                chequeo_casillero(tablero_tateti, fila_casillero, columna_casillero)[1], tablero_tateti, 'X')
    else:
        pongo_letra(chequeo_casillero(tablero_tateti, fila_casillero, columna_casillero)[0],
                    chequeo_casillero(tablero_tateti, fila_casillero, columna_casillero)[1], tablero_tateti, 'O')

    if chequeo_termina(tablero_tateti) == 6:
        imprimir_tablero(tablero_tateti)
        break











