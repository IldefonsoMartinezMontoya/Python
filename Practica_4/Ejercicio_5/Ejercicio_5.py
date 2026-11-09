from Practica_4.Ejercicio_5.Ejercicio_5 import Cliente
clientes = {}

while True:
    print("Opciones")
    print("1. Añadir Cliente")
    print("2. Eliminar Cliente")
    print("3. Mostrar Cliente")
    print("4. Listar Clientes")
    print("5. Listar Preferentes")
    print("6. Salir")

    opcion = int(input("Ingrese la opción: "))

    match opcion:
        case 1:
            print("Añadir Cliente")
            NIF = str(input("Ingrese NIF: "))
            nombre = str(input("Ingrese nombre: "))
            direccion = str(input("Ingrese direccion: "))
            telefono = str(input("Ingrese telefono: "))
            correo = str(input("Ingrese correo: "))
            preferente = bool(input("Ingrese preferente(True/False): "))
            clientes.update({NIF: Cliente(nombre, direccion, telefono, correo, preferente)})
        case 2:
            print("Eliminar Cliente")
            NIF = str(input("Ingrese NIF: "))
            clientes.pop(NIF)
        case 3:
            print("Mostrar Clientes")
            NIF = str(input("Ingrese NIF: "))
            print(clientes[NIF])
        case 4:
            print("Listar Clientes")
            for clave, valor in clientes.items():
                print(clave, valor)
        case 5:
            print("Listar Preferentes")
            for nif, cliente in clientes.items():
                if cliente.preferente:
                    print(nif, cliente)
        case 6:
            print("Saliendo")
            break
