class CuentaBancaria:
    def __init__(self, numero_cuenta, propietario, balance):
        self.numero_cuenta = numero_cuenta
        self.propietario = propietario
        self.balance = balance

    def depositar(self, deposito):
        if deposito > 0:
            self.balance += deposito
            print(f"Se depositaron {deposito} unidades en la cuenta.")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def aplicar_cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance -= cuota_manejo
        print(f"Se aplicó una cuota de manejo del 2% sobre el balance. Nuevo balance: {self.balance}")

    def mostrar_detalles(self):
        print("Detalles de la cuenta bancaria:")
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietario:", self.propietario)
        print("Balance:", self.balance)


propietario = input("Ingrese el nombre del propietario: ")
numero_cuenta = int(input("Ingrese el número de cuenta: "))
balance_inicial = float(input("Ingrese el balance de la cuenta: "))


cuenta = CuentaBancaria(numero_cuenta, propietario, balance_inicial)


cantidad_deposito = float(input("Ingrese la cantidad a depositar: "))
cuenta.depositar(cantidad_deposito)


cuenta.aplicar_cuota_manejo()

cuenta.mostrar_detalles()
