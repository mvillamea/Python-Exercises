import subprocess
import math
import sys

#raiz n-esima en python
def nth_root(radicand, n):
    return radicand **(1/n)

#da el ordinal en inglés


def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'

def ordinal(value):
    return str(value) + ordinal_suffix(value)

radicand = input('ingrese radicando ')
n = input( 'ingrese exponente ') 

def display_nth_root(radicand, n):
    root = nth_root(radicand, n)
    message = "The " + ordinal(n) + " root of "\
              + str(radicand) + " is " + str(root)
    print(message)
