abecedario = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sin3 = []
for indice, x in enumerate(abecedario):
    if (indice  + 1) % 3 == 0:
        abecedario.remove(x)
    else :
        sin3.append(x)
print(sin3)