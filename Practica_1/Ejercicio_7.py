num = int()
valido = True
while valido:
    num = int(input())
    if num % 2 != 0:
        valido = False
    if valido == False:
        break