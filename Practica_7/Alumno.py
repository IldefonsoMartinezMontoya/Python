class Alumno:
    def __init__(self, nombre: str, nota: int):
        self._nombre = nombre
        self._nota = nota
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
    def nota(self):
        return self._nota
    @nota.setter
    def nota(self, nota):
        if not nota:
            raise Exception("El dirección no puede estar vacío")
        else:
            self.nota = nota
    def __str__(self):
        if self._nota > 5:
            estado = "Aprobado"
        else:
            estado = "Suspenso"
        return f"Nombre: {self._nombre}, Nota: {self._nota}, {estado}"

a1 = Alumno("A", 0)
a2 = Alumno("B", 1)

print(a1)
print(a2)