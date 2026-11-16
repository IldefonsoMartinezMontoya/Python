letrica = input("Introduce una letra ")
def SioNo(letra):
    match letrica.lower():
        case "a" | "e" | "i" | "o" | "u":
            return "No"
        case "b" | "c" | "d" | "f" | "g" | "h" | "j" | "k" | "l" | "m" | "n" | "ñ" | "p" | "q" | "r" | "s" | "t" | "v" | "w" | "x" | "y" | "z":
            return "Si"
        case _:
            return "No letra"
print(SioNo(letrica))