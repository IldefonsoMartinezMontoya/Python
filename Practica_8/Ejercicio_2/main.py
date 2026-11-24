from .Banco import Banco
from .Cliente import Cliente


def main():
    cliente1 = Cliente("Ana", 100)
    cliente2 = Cliente("Luis", 250)
    cliente3 = Cliente("Marta", 80)

    banco = Banco(cliente1, cliente2, cliente3)
    banco.operar()
    banco.deposito_total()


if __name__ == "__main__":
    main()
