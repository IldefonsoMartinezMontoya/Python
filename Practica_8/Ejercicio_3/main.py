from .CajaAhorro import CajaAhorro
from .PlazoFijo import PlazoFijo


def main():
    caja = CajaAhorro("Ana López", 1500)
    plazo_fijo = PlazoFijo("Luis Pérez", 3000, 90, 5)

    caja.mostrar_informacion()
    print()
    plazo_fijo.mostrar_informacion()


if __name__ == "__main__":
    main()
