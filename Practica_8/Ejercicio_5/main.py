from .validacion_contrasena import validar_contrasena


def main():
    contrasena = input("Introduce una contraseña: ")
    resultado = validar_contrasena(contrasena)
    if resultado is True:
        print(True)
    else:
        print(resultado)


if __name__ == "__main__":
    main()
