num = float(input("Dame un numero: "))
if num >= 1000000:
    print("El numero debe ser inferior a un millón")
else:
    print(
        "Días:", num // 86400,
        "Horas:", (num % 86400) // 3600,
        "Minutos:", (num % 3600) // 60,
        "Segundos:", num % 60
    )