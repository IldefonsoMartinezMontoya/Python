palindromo = str(input("Ingrese un palindromo: ")).strip().upper().replace(" ", "")
if palindromo[0::] == palindromo[::-1]:
    print("Es palindromo")
else :
    print("No es palindromo")