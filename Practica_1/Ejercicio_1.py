num = int(input("Ingrese un numero: "))

if num % 2 == 0: print(num, "es divisible por 2")
else:
    if num % 3 == 0: print(num, "es divisible por 3")
    else:
        if num % 5 == 0: print(num, "es divisible por 5")