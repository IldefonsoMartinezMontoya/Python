verdadero = True
while verdadero:
    palabra = input("Ingrese una palabra: ")
    conjugacion = palabra[-2:]
    if conjugacion != "ar":
        print("Ingrese una palabra válida(pista: primera conjugación)")
    else:
        print("Yo", palabra[:-2] + "o")
        print("Tu", palabra[:-2] + "as")
        print("El/Ella", palabra[:-2] + "a")
        print("Nosotros", palabra[:-2] + "amos")
        print("Vosotros", palabra[:-2] + "ais")
        print("Ellos", palabra[:-2] + "an")
        verdadero = False