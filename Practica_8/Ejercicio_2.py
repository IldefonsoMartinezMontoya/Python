class Cliente:
    def __init__(self, nombre, cantidad: int):
        self.nombre = nombre
        self.cantidad = cantidad

    def depositar(self, deposito):
        self.cantidad += deposito
        return self.cantidad

    def extraer(self, deposito):
        self.cantidad -= deposito
        return self.cantidad

    def mostrar(self):
        print(self.cantidad)
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise Exception("El nombre no puede estar vacío")
        else:
            self._nombre = nombre

    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self, cantidad):
        if cantidad < 0:
            raise Exception("La cantidad no puede ser negativa")
        else:
            self._cantidad = cantidad
class Banco:
    def __init__(self, c1, c2, c3):
        self._c1 = c1
        self._c2 = c2
        self._c3 = c3

