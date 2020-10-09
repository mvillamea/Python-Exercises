import math

class Punto:
    def __init__(self, X = 0, Y = 0):
        self.coord_X = X
        self.coord_Y = Y

    def __str__(self):
       print("(", self.coord_X, ",", self.coord_Y, ")")

    def cuadrante(self):
        if self.coord_X == 0 and self.coord_Y != 0:
            return "El punto está en el eje y."
        elif self.coord_Y == 0 and self.coord_X != 0:
            return "El punto está en el eje x."
        elif self.coord_Y == 0 and self.coord_X == 0:
            return "El punto está en el origen."
        elif self.coord_X > 0 and self.coord_Y > 0:
            return "El punto está en el primer cuadrante."
        elif self.coord_X < 0  and self.coord_Y > 0:
            return "EL punto está en el segundo cuadrante."
        elif self.coord_X < 0 and self.coord_Y < 0:
            return "El punto está en el tercer cuadrante."
        else:
            return "El punto está en el cuarto cuadrante."

    def vector(self, otro_punto):
        parte_X = otro_punto.coord_X - self.coord_X
        parte_Y = otro_punto.coord_Y - self.coord_Y
        print ("El vector entre A y B es ", (parte_X , parte_Y))

    def distancia(self, otro_punto):
        parte_X = otro_punto.coord_X - self.coord_X
        parte_Y = otro_punto.coord_Y - self.coord_Y
        return math.sqrt(parte_X**2+parte_Y**2)


class Rectangulo:
    def __init__(self, puntoInicial = Punto(), puntoFinal= Punto()):
        self.puntoInicial = puntoInicial
        self.puntoFinal = puntoFinal
        self.b = puntoFinal.coord_X-puntoInicial.coord_X
        self.h = puntoFinal.coord_Y-puntoInicial.coord_Y

    def base (self):
        print ("La base del rectángulo es",self.b)


    def altura (self):
        print ("La altura del rectángulo es", self.h)


    def area(self):
        a = self.b*self.h
        print("El área del rectángulo es", a)


A = Punto(2,3)
B = Punto(5,5)

R = Rectangulo(A, B)
R.base()
R.altura()
R.area()
