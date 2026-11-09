nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
direccion = str(input("Ingrese su direccion: "))
telefono = str(input("Ingrese su telefono: "))
persona = {
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
          }
print(persona["nombre"], "tiene " + str(persona["edad"]) + " años, vive en", persona["direccion"], "y su número de teléfono es " + str(persona["telefono"]))