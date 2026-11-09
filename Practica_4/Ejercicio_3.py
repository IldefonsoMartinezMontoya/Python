import re

verdadero = True
while verdadero:
    fecha = str(input("Ingresa una fecha: "))
    if re.fullmatch(r"\d{2}/\d{2}/\d{4}", fecha):
        match fecha[3:5]:
            case "01":
                print(fecha[:2], "de Enero de", fecha[6:10])
            case "02":
                print(fecha[:2], "de Febrero de", fecha[6:10])
            case "03":
                print(fecha[:2], "de Marzo de", fecha[6:10])
            case "04":
                print(fecha[:2], "de Abril de", fecha[6:10])
            case "05":
                print(fecha[:2], "de Mayo de", fecha[6:10])
            case "06":
                print(fecha[:2], "de Junio de", fecha[6:10])
            case "07":
                print(fecha[:2], "de Julio de", fecha[6:10])
            case "08":
                print(fecha[:2], "de Agosto de", fecha[6:10])
            case "09":
                print(fecha[:2], "de Septiembre de", fecha[6:10])
            case "10":
                print(fecha[:2], "de Octubre de", fecha[6:10])
            case "11":
                print(fecha[:2], "de Noviembre de", fecha[6:10])
            case "12":
                print(fecha[:2], "de Deciembre de", fecha[6:10])
        verdadero = False
    else :
        fecha = str(input("Ingresa una fecha: "))
