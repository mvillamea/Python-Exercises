import subprocess
import math
import sys

#Dado un número n por consola, decide si es perfecto o no

def sumaDivisores(m):
    i=1
    sum=0
    while i<m:
        if (m%i)==0:
            sum=sum+i
        else:
            sum=sum
        i=i+1
    return sum


def DecideSiEsPerfecto(m):
    if m == sumaDivisores(m):
        print ('Es perfecto')
    else:
        print ('No es perfecto')


def main(m):
    DecideSiEsPerfecto(m)


if __name__ == '__main__':
    main( int(sys.argv[1]) )


