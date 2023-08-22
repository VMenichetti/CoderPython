from paquete1.modulo1 import *
from paquete1.modulo2 import Cliente


# Crear instancias de clientes
cliente1 = Cliente("Juan Pablo Menichetti", "jpmenichetti13@gmail.com", "Calle San Lorenzo 500", 1000)
cliente2 = Cliente("Santiago Molina", "santimome@gmail.com", "El Cardenal 1250", 1500)

# Mostrar información de los clientes
print(cliente1)
print(cliente2)

# Realizar compras y agregar saldo
print(cliente1.comprar(500))
print(cliente2.agregar_saldo(200))