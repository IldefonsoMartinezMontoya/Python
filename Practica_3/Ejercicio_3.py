asignaturas = ["matemáticas", "física", "química", "historia", "lengua"]
notas = []
for x in asignaturas:
    nota = int(input("Que nota has sacado en " + x + ": "))
    notas.append(nota)
for x, y in zip(asignaturas, notas):
    print(f"En {x} has sacado {y}")