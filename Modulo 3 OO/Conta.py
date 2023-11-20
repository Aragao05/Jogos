class Conta:

    #Atributos
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    #Metodos
    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))
    
    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

conta = Conta(123, "Vini", 55.0, 1000.0)
conta2 = Conta(321, "Claudio", 100.50, 3500.0)

conta.deposita(50.50)
conta.extrato()
conta.saca(15)
conta.extrato()