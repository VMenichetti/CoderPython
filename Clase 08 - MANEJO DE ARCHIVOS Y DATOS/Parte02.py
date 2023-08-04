persona = {
    "nombre" : None,
    "apellido" : None,
    "edad" : None

}

for dato in persona.keys():
  persona [dato] = input (f"Ingrese su {dato}: ")

f = open('C:\Users\Carlitox\Desktop\PYTHON\PRACTICAS PYTHON\Clase 08 - MANEJO DE ARCHIVOS Y DATOS\texto.txt', 'w')

for valor in persona.values():
  f.write(valor + "")

f.close