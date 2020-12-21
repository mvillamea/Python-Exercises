import subprocess
import math
import sys

#Determina el número y la longitud de la meseta más larga de una secuencia de números enteros

sec = [1, 1, 2, 2, 4, 4, 4]
NumActual=-1
NumMax= 999
LongActual= 0
LongMax= 0
i=0

while i<len(sec):

    if NumActual == sec[i]:
        LongActual=LongActual+1

    else :
        LongActual=1

    if LongMax<LongActual :
        LongMax=LongActual
        NumMax=sec[i]

    else :
        LongMax= LongMax

    NumActual=sec[i]
    i=i+1

print (NumMax , LongMax)



