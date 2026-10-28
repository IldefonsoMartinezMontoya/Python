nombre = str(input("Ingrese nombre: "))

if len(nombre) < 4: print(nombre, "es corto")
else:
    if len(nombre) > 4:
        print(nombre, "es largo")
        if " " in nombre:
            print(nombre, "es compuesto")