class Cliente:
    def __init__(self, nombre, cantidad=0):
        self.nombre = nombre
        self.cantidad = cantidad

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("El depósito debe ser mayor que cero")
        self.cantidad += cantidad

    def extraer(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        if cantidad > self.cantidad:
            raise ValueError("No hay saldo suficiente")
        self.cantidad -= cantidad

    def mostrar_total(self):
        print(f"Saldo de {self.nombre}: {self.cantidad} euros")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre.strip()

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = cantidad
