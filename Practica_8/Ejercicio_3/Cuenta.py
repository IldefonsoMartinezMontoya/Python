class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar_datos(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad} euros")

    def __str__(self):
        return f"Titular: {self.titular}, cantidad: {self.cantidad} euros"
