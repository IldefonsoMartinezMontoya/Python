while True:
    try:
        a = int(input("Introduce un numero entero: "))
        break
    except ValueError:
        print("No es entero")
