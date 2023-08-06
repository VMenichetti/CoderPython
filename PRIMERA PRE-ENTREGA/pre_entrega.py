"-->REGISTRO"

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

"-->GUARDADO"

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
    with open("lista_de_usuarios.txt", "a") as file:
        for usuario in lista_usuarios:
            file.write(f"{usuario['usuario']},{usuario['contraseña']}\n")

def main():
    print("Bienvenido al registro de usuarios y contraseñas.")
    lista_usuarios = guardar_en_lista()
    guardar_en_archivo(lista_usuarios)
    print("Usuarios y contraseñas guardados en lista_de_usuarios.")

    print("\nInicie sesión:")
    login(lista_usuarios)

if __name__ == "__main__":
    main()

"--> LOGIN"
"# Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario"
"# Verificar que el usuario este registrado y darle el ok cuando ingrese datos almacenados"
"# Si no esta registrado, dar la opcion de volver a registro"

def login(usuarios):
    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        for user in usuarios:
            if user['usuario'] == usuario and user['contraseña'] == contraseña:
                print("¡Inicio de sesión exitoso!")
                return
        print("Credenciales incorrectas. Inténtelo nuevamente.")

