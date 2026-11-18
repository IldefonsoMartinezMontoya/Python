class Triangulo:
    def __init__(self, lado1: float, lado2: float, lado3: float):
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            raise ValueError("Los lados deben ser mayores que cero.")
        if (lado1 + lado2 <= lado3 or
                lado1 + lado3 <= lado2 or
                lado2 + lado3 <= lado1):
            raise ValueError("Las medidas indicadas no forman un triángulo.")

        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self) -> float:
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self) -> str:
        if self.lado1 == self.lado2 == self.lado3:
            return "equilátero"
        elif (self.lado1 == self.lado2 or
              self.lado1 == self.lado3 or
              self.lado2 == self.lado3):
            return "isósceles"
        else:
            return "escaleno"


if __name__ == "__main__":
    try:
        lado1 = float(input("Introduce el primer lado: "))
        lado2 = float(input("Introduce el segundo lado: "))
        lado3 = float(input("Introduce el tercer lado: "))

        triangulo = Triangulo(lado1, lado2, lado3)
        print(f"Lado mayor: {triangulo.lado_mayor()}")
        print(f"Tipo de triángulo: {triangulo.tipo_triangulo()}")
    except ValueError as error:
        print(f"Error: {error}")
