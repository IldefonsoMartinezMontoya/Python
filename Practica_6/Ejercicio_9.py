def comprobarEdad(edad):
    if edad < 0:
        raise ValueError("El numero no puede ser negativo")
    elif edad > 120:
        raise ValueError("El numero no puede ser mayor de 120")
num = int(input("Ingrese un numero: "))
try:
    comprobarEdad(num)
except ValueError as e:
    print(f"Error: {e}")