class Conta:

    #Atributos
    #se o atributo tem "__"no nome ele é privado 
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Metodos
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))
    
    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

conta = Conta(123, "Vini", 55.0, 1000.0)
conta2 = Conta(321, "Claudio", 100.50, 3500.0)

conta.deposita(50.50)
conta.extrato()
conta.saca(15)
conta.extrato()