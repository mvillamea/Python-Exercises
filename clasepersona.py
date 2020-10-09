class Persona:
    def __init__(self, nombre = "", edad = int(), dni = int()):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print("nombre=", self.nombre, "edad=", self.edad, "dni=", self.dni)

    def esMayorDeEdad(self):
        return self.edad >= 18

class Cuenta:
    def __init__(self, titular = Persona(), cantidad = float()):
        self.titular = titular
        self._cantidad = cantidad

    def mostrar(self):
        print("Titular:", self.titular, "Cantidad de dinero en cuenta:", self._cantidad)

    def ingresar(self):
        cant_nueva = float(input("Ingrese dinero:"))
        if cant_nueva < 0:
            return
        else:
            self._cantidad = self._cantidad + cant_nueva
            return self._cantidad

    def retirar(self):
        cant_nueva = float(input("Ingrese la cantidad de dinero que desea retirar:"))
        self._cantidad = self._cantidad - cant_nueva
        return self._cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def esTitularValido(self):
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()

    def retirar(self):
        if self.esTitularValido():
            cant_nueva = float(input("Ingrese la cantidad de dinero que desea retirar:"))
            self._cantidad = self._cantidad - cant_nueva
            return self._cantidad
        else:
            return self._cantidad

    def mostrar(self):
        print("Cuenta joven", self.bonificacion)


mirna = Persona("Mirna", 22, 38765999)
hola = Cuenta(mirna, 400)
holajoven = CuentaJoven(mirna, 400, "5%")

holajoven.retirar()













