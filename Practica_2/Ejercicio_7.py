expresion = input("Ingrese una operación (por ejemplo, 8+3): ").replace(" ", "")

if len(expresion) != 3 or not expresion[0].isdigit() or not expresion[2].isdigit():
    print("Formato incorrecto. Use una cifra, un operador y otra cifra (por ejemplo, 8+3).")
else:
    a = int(expresion[0])
    operador = expresion[1]
    b = int(expresion[2])

    if operador == "+":
        resultado = a + b
    elif operador == "-":
        resultado = a - b
    elif operador == "*":
        resultado = a * b
    elif operador == "/":
        if b == 0:
            resultado = None
            print("No se puede dividir entre cero.")
        else:
            resultado = a / b
    else:
        resultado = None
        print("Operador no válido. Use +, -, * o /.")

    if resultado is not None:
        print("Resultado:", resultado)
