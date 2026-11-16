numerin = int(input("Introduce un numero: "))
def Facto(n):
    resultadoFacto = 1
    for i in range(n, 0, -1):
        resultadoFacto = resultadoFacto * i
    return resultadoFacto
print(Facto(numerin))