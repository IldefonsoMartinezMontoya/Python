num = str()
i = 0
total = 0
valido = True
while valido:
    num = input()
    if num == "":
        valido = False
    else:
        i += 1
        total += int(num)
    if valido == False:
        break
print ("Se han introducido", i, " numeros")
print ("El total es: ", total)