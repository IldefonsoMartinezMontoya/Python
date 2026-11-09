from xxlimited_35 import Str


class Cliente:
    def __init__(self, nombre: str, direccion:str, telefono: str, correo: str, preferente: bool):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.preferente = preferente

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise Exception("El nombre no puede estar vacio")
        else :
            self._nombre = nombre
    @property
    def direccion(self):
        return self._direccion
    @direccion.setter
    def direccion(self, direccion):
        if not direccion:
            raise Exception("El direccion no puede estar vacio")
        else :
            self._direccion = direccion
    @property
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono(self, telefono):
        if not telefono:
            raise Exception("El telefono no puede estar vacio")
        else :
            self._telefono = telefono
    @property
    def correo(self):
        return self._correo
    @correo.setter
    def correo(self, correo):
        if not correo:
            raise Exception("El correo no puede estar vacio")
        else :
            self._correo = correo
    @property
    def preferente(self):
        return self._preferente
    @preferente.setter
    def preferente(self, valor):
        self._preferente = valor