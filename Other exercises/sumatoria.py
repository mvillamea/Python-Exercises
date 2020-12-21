import subprocess
import math
import sys

#Dado un número n por consola, calcula la sumatoria desde 1 hasta n


n=int(sys.argv[1])
i = 1 
sum = 0


while i<=n:
    sum = sum+i
    i = i+1
print (sum)
