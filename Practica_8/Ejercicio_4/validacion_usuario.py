def validar_usuario(nombre):
    if len(nombre) < 6:
        return "El nombre de usuario debe contener al menos 6 caracteres"
    if len(nombre) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres"
    if not nombre.isalnum():
        return "El nombre de usuario puede contener solo letras y números"
    return True
