import subprocess
import math
import sys
from math import floor

#imprime del 1 al 100 en millas y su correspondiente conversión en km

mi = 0
km = 0

while mi<=100 :
	km = round(1.61*mi)
	print mi , km
	mi = mi+10



