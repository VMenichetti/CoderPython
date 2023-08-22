class Cliente:
    def __init__(self, nombre, email, direccion, saldo):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.saldo = saldo
    
    def comprar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return f"{self.nombre} ha realizado una compra de ${monto}. Saldo restante: ${self.saldo}"
        else:
            return f"{self.nombre} no tiene saldo suficiente para esta compra."
    
    def agregar_saldo(self, cantidad):
        self.saldo += cantidad
        return f"Se han agregado ${cantidad} al saldo de {self.nombre}. Saldo actual: ${self.saldo}"
    
    def __str__(self):
        return f"Cliente: {self.nombre}\nEmail: {self.email}\nDirección: {self.direccion}\nSaldo: ${self.saldo}"
