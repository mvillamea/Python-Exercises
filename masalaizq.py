import subprocess
import math
import sys

#Dada una lista decide si es más a la izquierda o no

def comparacion(s):
    medio=int((len(s)-1)//2)
    if s[0:(medio+1)]>s[(medio+1):(len(s))]:
        comparacion(s[0:(medio+1)]) and comparacion(s[(medio+1):(len(s))]) 
        return 'Es más a la izquierda'
    else:
        return 'No es más a la izquierda'
    

def main(s):
    print (comparacion(s))



if __name__ == '__main__':
    #main([1, 2, 3, 4])
    main ([8, 6, 7, 4, 5, 1, 8, 2])
