lista = [3, "a", 5, None, 7]
cuentaIgnorados = 0
suma = 0
for i in lista:
    try:
        suma = suma + i
    except:
        cuentaIgnorados += 1
print(cuentaIgnorados)
print(suma)
