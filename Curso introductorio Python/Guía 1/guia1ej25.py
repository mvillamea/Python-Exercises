"""Crear un programa que, a partir de una lista con todas las letras del abecedario, haga
un copia y borre de esta última todas las vocales. Luego imprimir por pantalla ambas
listas, la completa y la sin vocales."""

from string import ascii_lowercase
lista_abc = list(ascii_lowercase)
copia_lista_abc = lista_abc.copy()
print(lista_abc)
copia_lista_abc.remove('a')
copia_lista_abc.remove('e')
copia_lista_abc.remove('i')
copia_lista_abc.remove('o')
copia_lista_abc.remove('u')
print(copia_lista_abc)





