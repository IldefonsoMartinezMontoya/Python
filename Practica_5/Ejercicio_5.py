lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [11, 22, 33, 44, 5, 66, 77, 88, 99, 100]
def Igual(lista, lista2):
    for x in lista:
        if x in lista2:
            return True
    return False
print(Igual(lista1, lista2))