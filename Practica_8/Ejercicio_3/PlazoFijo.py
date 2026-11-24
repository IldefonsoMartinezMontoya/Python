from .Cuenta import Cuenta


class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def obtener_interes(self):
        return self.cantidad * self.interes / 100

    def mostrar_informacion(self):
        total_interes = self.obtener_interes()
        print("Plazo fijo")
        print(f"Titular: {self.titular}")
        print(f"Plazo: {self.plazo} días")
        print(f"Interés: {self.interes}%")
        print(f"Total de interés: {total_interes} euros")
