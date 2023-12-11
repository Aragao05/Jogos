class Conta:

    #Atributos
    #se o atributo tem "__" ou "_" no nome ele é privado 
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Metodos
    #mostra o extarto da pessoa 
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))
    
    #desposita um valor na conta da pessoa 
    def deposita(self, valor):
        self.__saldo += valor

    #Ve se a pessoa tem saldo para saque
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar

    # Realiza o saque se tiver o valor se não mostra a mensagem 
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")

    #Se tiver o valor realiza a tranferencia para  conta de outra pessoa 
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property #usar @property para transformar um método de uma classe em um atributo somente de leitura. Isso oferece 
              #uma maneira de acessar um valor de maneira semelhante à leitura de um atributo, sem a necessidade de chamar 
              #explicitamente um método. 
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter # só pode ser usado quando houver um property, usado pra mudar o valor de um atributo
    def limite(self, limite):
        self.__limite = limite

    @staticmethod #um metodo que pode ser chamado sem fazer parte da classe em si
    def codigos_bancos(self):
        return {'NuBank': '001', 'C6 Bank': '104', 'Bradesco':'237'}

conta = Conta(123, "Vini", 55.0, 1000.0)
conta2 = Conta(321, "Claudio", 100.50, 3500.0)

conta.deposita(50.50)
conta.extrato()
conta.saca(15)
conta.extrato()