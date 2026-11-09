cesta = {}
coste = 0
while True:
    articulo = input("Ingrese el nombre del artículo (o 'Terminar' para salir): ")
    if articulo.strip().lower() == "terminar":
        break
    precio = float(input("Ingrese el precio del artículo: "))
    cesta[articulo] = precio
    coste += precio
for x, y in cesta.items():
    print(x, y)
    print("Total", coste)