import subprocess
import math
import sys

#Determina si una palabra dada es un palíndromo o no

def DarVuelta(palabra):
    tamano= len(palabra)
    i=tamano-1
    al_reves= ""

    while i>=0:
        al_reves=al_reves+palabra[i]
        i=i-1
    return al_reves


def main(palabra):

    if palabra==DarVuelta(palabra):
        print('Es palindromo')

    else :
        print('No es palindromo')

if __name__ == '__main__':
    main( sys.argv[1] )
