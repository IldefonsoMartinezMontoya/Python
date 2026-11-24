from Ejercicio_4.validacion_usuario import validar_usuario
from Ejercicio_5.validacion_contrasena import validar_contrasena


def main():
    nombre = input("Introduce un nombre de usuario: ")
    contrasena = input("Introduce una contraseña: ")

    resultado_usuario = validar_usuario(nombre)
    resultado_contrasena = validar_contrasena(contrasena)

    if resultado_usuario is True and resultado_contrasena is True:
        print("El nombre de usuario y la contraseña son válidos.")
    else:
        if resultado_usuario is not True:
            print(resultado_usuario)
        if resultado_contrasena is not True:
            print(resultado_contrasena)


if __name__ == "__main__":
    main()
