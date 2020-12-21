import subprocess
import math
import sys

#raiz n-esima en python

radicand = input('ingrese radicando ')
n = input( 'ingrese exponente ') 


def nth_root(radicand, n):
    return radicand **(1/n)

#if __name__ == '__main__':
 #   nth_root(radicand, n)
