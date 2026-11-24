from .validacion_usuario import validar_usuario


def main():
    nombre = input("Introduce un nombre de usuario: ")
    resultado = validar_usuario(nombre)
    if resultado is True:
        print(True)
    else:
        print(resultado)


if __name__ == "__main__":
    main()
