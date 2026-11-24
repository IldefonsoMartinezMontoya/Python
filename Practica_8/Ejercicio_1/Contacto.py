class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre.strip()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        if not telefono.strip():
            raise ValueError("El teléfono no puede estar vacío")
        self._telefono = telefono.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not email.strip():
            raise ValueError("El email no puede estar vacío")
        self._email = email.strip()

    def __str__(self):
        return f"Nombre: {self.nombre}, teléfono: {self.telefono}, email: {self.email}"
