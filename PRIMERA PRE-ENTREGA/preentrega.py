"-->REGISTRO"
# El usuario debe contener al menos 6 digitos
# La contraseña debe tener al menos 8 digitos, una mayuscula, minuscula y un numero

def crea_usuario():
    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        if len(usuario) >= 6:
            break
        else:
            print("El usuario debe contener al menos 6 dígitos")

    while True:
        contraseña = input("Ingrese su contraseña: ")
        if valida_contraseña(contraseña):
            rcontraseña = input("Vuelva a ingresar la contraseña: ")
            if contraseña == rcontraseña:
                break
            else:
                print("Las contraseñas no coinciden. Inténtelo nuevamente.")
        else:
            print("La contraseña debe tener al menos 8 dígitos, una mayúscula, una minúscula y un número.")

    persona = {
        "usuario": usuario,
        "contraseña": contraseña
    }

    return persona

# Verificamos que la contraseña cumpla con los criterios

def valida_contraseña(contraseña):
    if len(contraseña) < 8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero


def mostrar_usuario(persona):
    print("Usuario creado con éxito:")
    print(persona)

persona = crea_usuario()
mostrar_usuario(persona)

"--> Almacenamiento de usuarios"

def guardar_en_lista():
    lista_usuarios = []
    while True:
        nuevo_usuario = crea_usuario()
        lista_usuarios.append(nuevo_usuario)
        opcion = input("¿Desea agregar otro usuario? (si/no): ")
        if opcion.lower() != 'si':
            break
    return lista_usuarios

def guardar_en_archivo(lista_usuarios):
    with open("usuarios.txt", "w") as file:
        for usuario in lista_usuarios:
            file.write(f"{usuario['usuario']},{usuario['contraseña']}\n")

def main():
    print("Bienvenido al registro de usuarios y contraseñas.")
    lista_usuarios = guardar_en_lista()
    guardar_en_archivo(lista_usuarios)
    print("Usuarios y contraseñas guardados en usuarios.txt.")



"--> LOGIN"


def guardar_en_txt(persona):
    with open("usuario.txt", "w") as archivo:
        archivo.write(f"Usuario: {persona['usuario']}\n")
        archivo.write(f"Contraseña: {persona['contraseña']}\n")

guardar_en_txt(persona)

