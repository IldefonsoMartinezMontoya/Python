facturas = {}
cobrado = 0

while True:
    print("\nOpciones")
    print("1. Añadir una factura")
    print("2. Pagar una factura")
    print("3. Terminar")

    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            numero = input("Ingrese el número de factura: ")
            if numero in facturas:
                print("Ya existe una factura con ese número")
            else:
                coste = float(input("Ingrese el coste de la factura: "))
                facturas[numero] = coste

        case "2":
            numero = input("Ingrese el número de factura a pagar: ")
            if numero in facturas:
                cobrado += facturas.pop(numero)
                print("Factura pagada")
            else:
                print("No existe una factura con ese número")

        case "3":
            print("Terminando")
            break

        case _:
            print("Opción no válida")

    pendiente = sum(facturas.values())
    print("Cantidad cobrada hasta el momento:", cobrado)
    print("Cantidad pendiente de cobro:", pendiente)
