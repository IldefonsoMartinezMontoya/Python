num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
try:
    div = num1 / num2
except ZeroDivisionError:
    print("No se puede dividir por 0")
else :
    print(div)
finally:
    print("Fin de operación")