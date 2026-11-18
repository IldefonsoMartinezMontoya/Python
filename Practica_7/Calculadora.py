class Calculadora:
    def __init__(self, numero1: int, numero2: int):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self) -> int:
        return self.numero1 + self.numero2

    def restar(self) -> int:
        return self.numero1 - self.numero2

    def multiplicar(self) -> int:
        return self.numero1 * self.numero2

    def dividir(self) -> float:
        if self.numero2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return self.numero1 / self.numero2


if __name__ == "__main__":
    numero1 = int(input("Introduce el primer número entero: "))
    numero2 = int(input("Introduce el segundo número entero: "))

    calculadora = Calculadora(numero1, numero2)
    print(f"Suma: {calculadora.sumar()}")
    print(f"Resta: {calculadora.restar()}")
    print(f"Multiplicación: {calculadora.multiplicar()}")

    try:
        print(f"División: {calculadora.dividir()}")
    except ZeroDivisionError as error:
        print(error)
