import math

peso = float(input("Ingrese el peso(en Kg): "))
estatura = int(input("Ingrese el estatura(en cm): "))

imc = peso / (math.pow((estatura / 100), 2))

print ("El imc del peso es: ", round(imc, 2))