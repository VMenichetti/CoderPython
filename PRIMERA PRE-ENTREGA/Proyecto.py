usuario=input("Ingrese su nombre de usuario: ")
contraseña=input("Ingrese su contraseña: ")
rcontraseña=input("Vuelva a ingresar la contraseña: ")

# la contraseña debe tener al menos 8 digitos, una mayuscula, minuscula y un numero
# el usuario debe contener al menos 6 digitos

def crea_usuario():
    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        if len(usuario) >= 6:
            break
        else:
            print("El usuario debe contener al menos 6 dígitos.")

        
        
persona={
    "usuario": usuario,
    "contraseña": contraseña
}

persona = crea_usuario()
print("Usuario creado con éxito!")
print(persona)