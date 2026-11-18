class Persona:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise Exception("El nombre no puede estar vacio")
        else:
            self._nombre = nombre
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if not edad:
            raise Exception("El direccion no puede estar vacio")
        else:
            self._edad = edad

    def __str__(self):
        if self._edad >= 18:
            estado = "Mayor de edad"
        else:
            estado = "Menor de edad"
        return f"Nombre: {self._nombre}, Nota: {self._edad}, {estado}"
p1 = Persona("P1", 18)
p2 = Persona("P2", 15)
print(p1)
print(p2)