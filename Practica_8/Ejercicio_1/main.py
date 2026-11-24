from .Agenda import Agenda


def main():
    agenda = Agenda()

    while True:
        print("\nQué quieres hacer?")
        print("1. Añadir contacto")
        print("2. Lista de contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Cerrar agenda")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            try:
                agenda.anadir_contacto(nombre, telefono, email)
                print("Contacto añadido.")
            except ValueError as error:
                print(error)
        elif opcion == "2":
            agenda.listar_contactos()
        elif opcion == "3":
            nombre = input("Nombre que quieres buscar: ")
            contacto = agenda.buscar_contacto(nombre)
            print(contacto if contacto else "No se encontró ese contacto.")
        elif opcion == "4":
            nombre = input("Nombre del contacto que quieres editar: ")
            campo = input("Campo (nombre, teléfono o email): ")
            valor = input("Nuevo valor: ")
            try:
                if agenda.editar_contacto(nombre, campo, valor):
                    print("Contacto actualizado.")
                else:
                    print("No se encontró el contacto o el campo no es válido.")
            except ValueError as error:
                print(error)
        elif opcion == "5":
            print("Agenda cerrada.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
