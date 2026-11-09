Fruta = {
    "Platano":1.35,
    "Manzana":0.80,
    "Pera":0.85,
    "Naranja":0.70
}
pregunta = str(input("Que fruta quiere: "))
if pregunta in Fruta:
    print(Fruta[pregunta])
else :
    print("No ta")