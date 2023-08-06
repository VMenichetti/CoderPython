# el usuario debe contener al menos 6 digitos
# la contraseña debe tener al menos 8 digitos, una mayuscula, minuscula y un numero


def verificar_cuenta():
    try:
        with open("Lista_de_usuarios.txt", "r") as file:
            usuarios_registrados = set()
            for line in file:
                username, _ = line.strip().split(',')
                usuarios_registrados.add(username)
    except FileNotFoundError:
        # Si el archivo no existe, lo creamos en blanco
        with open("Lista_de_usuarios.txt", "w"):
            pass

    while True:
        opcion = input("¿Tienes una cuenta registrada? (s/n): ")
        if opcion.lower() == 's':
            iniciar_sesion()
            break
        elif opcion.lower() == 'n':
            usuario_nuevo = crea_usuario()
            with open("Lista_de_usuarios.txt", "a") as file:
                file.write(f"{usuario_nuevo['usuario']},{usuario_nuevo['contraseña']}\n")
            print("Usuario registrado exitosamente.")
            iniciar_sesion()
            break
        else:
            print("Opción inválida. Por favor, responda 's' o 'n'.")

def iniciar_sesion():
    while True:
        print("Bienvenido al login. ")
        usuario = input("Ingrese su nombre de usuario para login: ")
        contraseña = input("Ingrese su contraseña para login: ")

        with open("Lista_de_usuarios.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(',')
                if username == usuario and password == contraseña:
                    print("Inicio de sesión exitoso.")
                    # opcion = input("¿Desesa ver la lista de usuarios? (s/n)")
                    # if opcion.lower() == "s":
                        
                    return True

        print("Usuario inexistente. Intente nuevamente.")

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


def guardar_en_lista():
    lista_usuarios = []
    while True:
        nuevo_usuario = crea_usuario()
        lista_usuarios.append(nuevo_usuario)
        opcion = input("¿Desea agregar otro usuario? (s/n): ")
        if opcion.lower() != 's':
            break
    return lista_usuarios

def guardar_en_archivo(lista_usuarios):
    with open("Lista_de_usuarios.txt", "a") as file:
        for usuario in lista_usuarios:
            file.write(f"{usuario['usuario']},{usuario['contraseña']}\n")

# def lista():
#     print("Bienvenido al registro de usuarios y contraseñas.")
    
#     lista_usuarios = guardar_en_lista()
#     guardar_en_archivo(lista_usuarios)
#     print("Usuarios y contraseñas guardados en Lista_de_usuarios.txt.")

if __name__ == "__main__":
    verificar_cuenta()
#  iniciar_sesion()
    # lista()
