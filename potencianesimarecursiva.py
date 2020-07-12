import subprocess
import math
import sys

#Dados a, n naturales devuelve a^n recursivamente

def PotenciaNesima (a, n):

    if (a==n and n==0):
        print ('No esta definido')

    elif (a!=0 and n==0):
        return 1

    elif n==1:
        return a

    else:
        
        if n%2==0:
             MediaPotPar=PotenciaNesima(a, math.floor(n/2))
             return MediaPotPar*MediaPotPar
        else :
             MediaPotImpar=PotenciaNesima(a, math.ceil(n/2))
             return MediaPotImpar*MediaPotImpar
	
        

def main(a,n):
    print (PotenciaNesima(a,n))

if __name__ == '__main__':
    main( int(sys.argv[1]), int(sys.argv[2]) )
