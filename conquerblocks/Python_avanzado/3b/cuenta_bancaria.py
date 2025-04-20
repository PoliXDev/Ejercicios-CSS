
#Crea una clase "CuentaBancaria" con atributos como número de cuenta y 
#saldo. Implementa métodos para depositar y retirar dinero, y muestra el 
#saldo actual.

#clase cuenta bancaria
class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

#metodo para depositar dinero
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}")

#metodo para retirar dinero
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente para realizar el retiro.")
        else:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}")

#metodo para mostrar el saldo
    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta {self.numero_cuenta} es de {self.saldo}")

#ejemplo de uso
cuenta1 = CuentaBancaria("1234567890", 1000)
cuenta1.mostrar_saldo()
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.mostrar_saldo()

