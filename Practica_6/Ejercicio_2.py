try:
    a = int(input("Introduce un numero entero: "))
    b = int(input("Introduce otro numero entero: "))
    c = a / b
except ZeroDivisionError:
    print("No se puede dividir por 0")