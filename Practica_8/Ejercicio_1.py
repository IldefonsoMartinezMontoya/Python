class contacto:
    def __init__(self, nombre, telefono, email):
        self._nombre = nombre
        self._telefono = telefono
        self._email = email

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise Exception("El nombre no puede estar vacío")
        else:
            self._nombre = nombre

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        if not telefono:
            raise Exception("El telefono no puede estar vacío")
        else:
            self._telefono = telefono

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not email:
            raise Exception("El email no puede estar vacío")
        else:
            self._email = email

agenda = []

while True:
    print("Qué quieres hacer? Escribe una opción: ")
    print("Añadir contacto")
    print("Lista de contactos")
    print("Buscar contacto")
    print("Editar contacto")
    print("Cerrar agenda")
    opcion = input("Elige una opción: ")
    match opcion:
        case "Añadir contacto":
            nombre = input("El nombre del contacto: ")
            telefono = input("El teléfono del contacto: ")
            email = input("El email del contacto: ")
            agenda.append(contacto(nombre, telefono, email))
        case "Lista de contactos":
            for x in agenda:
                print(x)
        case "Buscar contacto":
            nombre = input("Nombre que quieres buscar: ").strip()
            encontrado = None
            for contacto in agenda:
                if contacto.nombre.casefold() == nombre.casefold():
                    encontrado = contacto
                    break

            if encontrado:
                print(encontrado)
            else:
                print("No se encontró ese contacto.")
        case "Editar contacto":
            nombre = input("Nombre del contacto que quieres editar: ").strip()
            encontrado = None
            for contacto in agenda:
                if contacto.nombre.casefold() == nombre.casefold():
                    encontrado = contacto
                    break

            if encontrado is None:
                print("No se encontró ese contacto.")
                continue

            print("¿Qué quieres editar? Escribe: Nombre, Telefono o Email")
            campo = input("Opción: ").strip().casefold()
            valor = input("Nuevo valor: ")
            try:
                match campo:
                    case "nombre":
                        encontrado.nombre = valor
                    case "telefono":
                        encontrado.telefono = valor
                    case "email":
                        encontrado.email = valor
                    case _:
                        print("Opción no válida.")
                        continue

                print("Contacto actualizado.")
            except ValueError as error:
                print(error)

        case "Cerrar agenda":
            print("Agenda cerrada.")
            break