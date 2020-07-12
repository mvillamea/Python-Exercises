import subprocess
import math
import sys

class Punto:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def distanciaAlOrigen(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

   

def main(a, b):
    p = Punto(a, b)
    print p.distanciaAlOrigen()


if __name__ == '__main__':
   
    main (2, 3)

