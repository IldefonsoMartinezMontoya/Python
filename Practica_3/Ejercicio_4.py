ganadores = []
verdadero = True
while verdadero:
    pregunta = int(input("Ingrese los números ganadores: "))
    if pregunta in ganadores:
        verdadero = False
    else :
        ganadores.append(pregunta)
ganadores.sort()
print(ganadores)