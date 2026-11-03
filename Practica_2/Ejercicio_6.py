num = float(input("Ingrese un numero: "))

billetes_100 = num // 100
resto100 = num % 100
billetes_50 = 0
resto50 = 0
billetes_20 = 0
resto20 = 0
biilletes_10 = 0
resto10 = 0
billetes_5 = 0
resto5 = 0
moneda_1 = 0
resto1 = 0
moneda_05 = 0
resto05 = 0
moneda_02 = 0
resto02 = 0
moneda_01 = 0
resto01 = 0
moneda_005 = 0
resto005 = 0
moneda_001 = 0
resto001 = 0
if resto100 >= 50:
    billetes_50 = resto100 // 50
    resto50 = resto100 % 50
    if resto50 >= 20:
        billetes_20 = resto50 // 20
        resto20 = resto50 % 20
        if resto20 >= 10:
            biilletes_10 = resto20 // 10
            resto10 = resto20 % 10
            if resto10 >= 5:
                billetes_5 = resto10 // 5
                resto5 = resto10 % 5
                if resto5 >= 1:
                    moneda_1 = resto5 // 1
                    resto1 = resto5 % 1
                    if resto1 >= 0.5:
                        moneda_05 = resto1 // 0.5
                        resto05 = resto1 % 0.5
                        if resto05 >= 0.20:
                            moneda_02 = resto05 // 0.20
                            resto02 = resto05 % 0.20
                            if resto02 >= 0.10:
                                moneda_01 = resto02 // 0.1
                                resto01 = resto02 % 0.1
                                if resto01 >= 0.05:
                                    moneda_005 = resto01 // 0.05
                                    resto005 = resto01 % 0.05
                                    if resto005 >= 0.01:
                                        moneda_001 = resto005 // 0.01
                                        resto001 = resto005 % 0.01
print("Billetes de 100:", billetes_100)
print("Billetes de 50", billetes_50)
print("Billetes de 20", billetes_20)
print("Billetes de 10", biilletes_10)
print("Billetes de 5", billetes_5)
print("Monedas de 1", moneda_1)
print("Monedas de 0.50", moneda_05)
print("Monedas de 0.20", moneda_02)
print("Monedas de 0.10", moneda_01)
print("Monedas de 0.05", moneda_005)
print("Monedas de 0.01", moneda_001)