num = str(input("Ingrese un numero: "))
decimal = 0
for i in range(len(num)):
    cifra = int(num[i])
    peso = 2 ** (len(num) - 1 - i)
    decimal += cifra * peso

print(decimal)