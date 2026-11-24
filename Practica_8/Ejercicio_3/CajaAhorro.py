from .Cuenta import Cuenta


class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        self.heredar_datos(titular, cantidad)

    def heredar_datos(self, titular, cantidad):
        super().__init__(titular, cantidad)

    def mostrar_informacion(self):
        print("Caja de ahorro")
        self.mostrar_datos()
