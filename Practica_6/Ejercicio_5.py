dicc = {"pan": 1.2, "leche": 0.9}
try:
    producto = str(input("Introduce un producto: "))
    print(dicc[producto])
except KeyError:
    print("Producto no encontrado")