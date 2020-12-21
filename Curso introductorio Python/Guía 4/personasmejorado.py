
escrito = """1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006"""


with open("personas1.txt", "w+") as f:
    """Esta función crea un archivo 
    con el escrito de arriba"""
    f.write(escrito)
    f.close()


def separo_datos(lista):
    """Dada una lista separamos
    sus elementos utilizando
    ; como separador"""
    datos = []
    for i in range(len(lista)):
        datos=datos.__add__(lista[i].split(sep=';'))
    return datos


def armo_lista(lista, n):
    """Dada una lista y una cantidad
    partimos esa lista en rangos de
    4n y 4n+4"""
    datos_n=[]
    for i in range(4*n, 4*n+4):
        datos_n=datos_n.__add__([lista[i]])
    return datos_n


def borro_saltos_linea(palabra):
    """borramos el escape de salto
    de linea de una palabra dada"""
    return palabra.replace('\n', '')


def saco_saltos_linea(lista):
    """Dada una lista con un elemento
     por posición, borramos todos los
     escapes de salto de linea
     de sus elementos"""
    for i in range(len(lista)):
        lista[i]=borro_saltos_linea(lista[i])
    return lista


def armo_diccionario(lista, n):
    """Dada una lista con datos de id,
    nombre, apellido y nacimiento y el
    número que la identifica, armamos un
    diccionario que contenga esos datos"""
    tupla_comun = ('id', 'nombre', 'apellido', 'nacimiento')
    tupla = tuple(armo_lista(lista, n))
    diccio = dict(zip(tupla_comun, tupla))
    return diccio


with open("personas1.txt","r") as personas:
    pers = personas.readlines()
    datos=separo_datos(pers)
    datos=saco_saltos_linea(datos)
    for i in range(4):
        print(armo_diccionario(datos,i))
    personas.close()

