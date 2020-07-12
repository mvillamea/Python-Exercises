import subprocess
import math
import sys

#Dado un número n por consola, calcula su factorial


n=int(sys.argv[1])
i = 1
fact = 1

while i<=n:
    fact = fact*i
    i = i+1
print (fact)




