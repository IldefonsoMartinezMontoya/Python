num = int(input("Ingrese un numero: "))
suma = num * (num + 1) / 2
for i in range(1, num + 1):
    print(i, end=" ")
print()
print(suma)