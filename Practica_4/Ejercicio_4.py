dick = {"esto":"this", "es":"is", "un":"a", "programa":"programm", "de":"of", "traducción":"traduction"}
texto = str(input("Ingrese un texto: ")).strip().lower()
for x in texto.split():
    print(dick.get(x, x), end=" ")