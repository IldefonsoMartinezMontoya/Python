verdadero = True
while verdadero:
    fecha = str(input("Ingrese un numero entre(10100 y 311299): "))
    numero = int(fecha)

    if numero < 10100 or numero > 311299:
        print("Ingrese un numero entre(10100 y 311299)")
    else:
        if len(fecha) == 6:
            print("Día:", fecha[:2], "Mes:", fecha[2:4], "Año: 20" + fecha[4:])
            verdadero = False
        elif len(fecha) == 5:
            print("Día:", fecha[:1], "Mes:", fecha[2:3], "Año: 20" + fecha[3:])
            verdadero = False