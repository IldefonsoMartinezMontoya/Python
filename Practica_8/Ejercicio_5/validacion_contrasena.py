def validar_contrasena(contrasena):
    segura = (
        len(contrasena) >= 8
        and any(letra.islower() for letra in contrasena)
        and any(letra.isupper() for letra in contrasena)
        and any(letra.isdigit() for letra in contrasena)
        and any(not letra.isalnum() and not letra.isspace() for letra in contrasena)
        and not any(letra.isspace() for letra in contrasena)
    )

    if segura:
        return True
    return "La contraseña elegida no es segura"
