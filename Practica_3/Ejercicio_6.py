asignaturas = ["matemáticas", "física", "química", "historia", "lengua"]
notas = []

for asignatura in asignaturas:
    nota = int(input(f"¿Qué nota has sacado en {asignatura}? "))
    notas.append(nota)

for asignatura, nota in zip(asignaturas, notas):
    print(f"En {asignatura} has sacado {nota}")

asignaturas = [
    asignatura
    for asignatura, nota in zip(asignaturas, notas)
    if nota < 5
]

print("Asignaturas que quedan:", asignaturas)