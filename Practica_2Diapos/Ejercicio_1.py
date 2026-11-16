asignaturas = {"SGEMP":10, "DEINT":6, "Inglés":10, "ACDAT":8}
for x, y in enumerate(asignaturas):
    if x == 1:
        asignaturas[y] = 0
asignaturas.update({"color":"rojo"})
print(asignaturas)
asignaturas.pop("color")
print(asignaturas)