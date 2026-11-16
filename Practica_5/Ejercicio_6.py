cadena = str(input("Ingrese cadena: "))

def Mayus(cadena):
    totalMayus = 0
    for letra in cadena:
        if letra.isupper():
            totalMayus += 1
    return totalMayus
print(Mayus(cadena))