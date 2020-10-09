"""En una determinada empresa, sus empleados son evaluados al final de cada año. Los
puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir
los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las
cifras mencionadas. A continuación se muestra una tabla con los niveles
correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel
es de 100000 multiplicada por la puntuación del nivel.
Nivel Puntuación
Inaceptable 0.0
Aceptable 0.4
Meritorio 0.6 o más
Crear un programa que lea la puntuación del usuario e indique su nivel de
rendimiento, así como la cantidad de dinero que recibirá el usuario."""

puntuacion = input("Ingrese la puntuación de le empleade: ")
puntuacion = float(puntuacion)

def nivel_e_ingresos(puntos):
    dinero = puntos * 100000
    if puntos == 0.0:
        print("El nivel es Inaceptable y la cantidad de dinero obtenida será ", dinero)
    elif puntos == 0.4:
        print("El nivel es Aceptable y la cantidad de dinero obtenida será ", dinero)
    elif puntos >= 0.6:
        print("El nivel es Meritorio y la cantidad de dinero obtenida será ", dinero)
    else:
        print("La puntuación ingresada no es válida")

nivel_e_ingresos(puntuacion)