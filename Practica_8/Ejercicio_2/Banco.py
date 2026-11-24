class Banco:
    def __init__(self, cliente1, cliente2, cliente3):
        self._c1 = cliente1
        self._c2 = cliente2
        self._c3 = cliente3

    def operar(self):
        for cliente in (self._c1, self._c2, self._c3):
            print(f"\nCliente: {cliente.nombre}")
            operacion = input("¿Quieres depositar o extraer? ").strip().casefold()
            try:
                cantidad = float(input("Cantidad: "))
                if operacion == "depositar":
                    cliente.depositar(cantidad)
                elif operacion == "extraer":
                    cliente.extraer(cantidad)
                else:
                    print("Operación no válida.")
                    continue
                cliente.mostrar_total()
            except ValueError as error:
                print(error)

    def deposito_total(self):
        total = self._c1.cantidad + self._c2.cantidad + self._c3.cantidad
        print(f"Dinero total en el banco: {total} euros")
        return total
