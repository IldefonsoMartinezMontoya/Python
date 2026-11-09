palabra = str(input("Ingrese una palabra: ")).strip(" ").upper()
cuentaA = 0
cuentaE = 0
cuentaI = 0
cuentaO = 0
cuentaU = 0
for x in palabra:
    match x:
        case "A":
            cuentaA += 1
        case "E":
            cuentaE += 1
        case "I":
            cuentaI += 1
        case "O":
            cuentaO += 1
        case "U":
            cuentaU += 1
print("Nummero de As:", cuentaA, "Nummero de Es:", cuentaE, "Numero de Is:", cuentaI, "Numero de Os:", cuentaO, "Numero de Us:", cuentaU)