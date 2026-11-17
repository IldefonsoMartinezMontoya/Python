diccionario = {"ilde":"634 48 20 23"}
while True:
    print("Ingrese Opción(1-3)")
    print("1. Consultar")
    print("2. Añadir")
    print("3. Salir")

    try:
        opcion = int(input("Ingrese opcion: "))
        match opcion:
            case 1:
                for x, y in diccionario.items():
                    print(x, y)
            case 2:
                nombre = input("Ingrese nombre: ")
                numero = (input("Ingrese numero: "))
                diccionario.update({nombre: numero})
            case 3:
                break
    except ValueError:
        print("Me da a mi que no")
    except KeyError:
        print("Me da a mi que no")
