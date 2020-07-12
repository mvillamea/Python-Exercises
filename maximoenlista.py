import subprocess
import math
import sys

#Dada una lista devuelve la posición de su máximo


def lugar_maximo(sec):

    if len(sec)==1:
        return 1
        

    elif len(sec)>1 :
        medio=int((len(sec)-1)//2)

        if max(sec[1:sec[medio]]) == sec[medio]:
            max_izq=medio

        if max(sec[1:sec[medio+1]]) != sec[medio]:
            lugar_maximo( sec[1:sec[medio-1]] )

        if max(sec[(sec[medio+1]):(len(sec)-1)]) == sec[medio+1]:  
            max_der=medio+1

        if max(sec[(sec[medio+1]):(len(sec)-1)]) != sec[medio+1]:
            lugar_maximo( sec[(sec[medio+2]):(len(sec)-1)])

        if sec[max_izq]>=sec[max_der]:
            return max_izq

        if sec[max_izq]<=sec[max_der]:
            return max_der

def main(sec):
    print (lugar_maximo(list(sec)))


if __name__ == '__main__':
    main([1, 3, 1, 1])
