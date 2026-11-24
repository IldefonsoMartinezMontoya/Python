from .Contacto import Contacto


class Agenda:
    def __init__(self):
        self.contactos = []

    def anadir_contacto(self, nombre, telefono, email):
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
            return

        for contacto in self.contactos:
            print(contacto)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.casefold() == nombre.strip().casefold():
                return contacto
        return None

    def editar_contacto(self, nombre, campo, valor):
        contacto = self.buscar_contacto(nombre)
        if contacto is None:
            return False

        campo = campo.strip().casefold()
        if campo == "nombre":
            contacto.nombre = valor
        elif campo in ("telefono", "teléfono"):
            contacto.telefono = valor
        elif campo == "email":
            contacto.email = valor
        else:
            return False
        return True
