asignaturas = ["matemáticas", "física", "química", "historia", "lengua"]
asignaturas.insert(3, "programación")
asignaturas.remove("matemáticas")
for x in asignaturas:
    print(x, end=" ")