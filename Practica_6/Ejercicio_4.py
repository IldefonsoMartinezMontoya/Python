lista = ["manzana", "pera", "limon", "aguacate"]
try:
    numero = int(input("Introduce una posición: "))
    print(lista[numero])
except IndexError:
    print("Tiene que ser una posición válida")