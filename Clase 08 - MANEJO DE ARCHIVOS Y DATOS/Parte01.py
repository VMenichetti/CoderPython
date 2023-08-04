texto = input ("Ingrese lo que quiere escribir: ")
f = open('C:\Users\Carlitox\Desktop\PYTHON\PRACTICAS PYTHON\Clase 08 - MANEJO DE ARCHIVOS Y DATOS\texto.txt', 'a')
f.write(texto)
f.close()  