hora = input("Ingrese la hora como hora,minuto,segundo (por ejemplo, 13,43,24): ")
partes = hora.split(",")

if len(partes) != 3:
    print("Formato incorrecto. Use hora,minuto,segundo.")
else:
    h, m, s = (int(parte.strip()) for parte in partes)

    if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
        print("Hora no válida.")
    else:
        s += 1
        if s == 60:
            s = 0
            m += 1
            if m == 60:
                m = 0
                h = (h + 1) % 24

        print(f"{h:02d},{m:02d},{s:02d}")
