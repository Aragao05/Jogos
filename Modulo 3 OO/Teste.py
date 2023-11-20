def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular,"saldo": saldo,"limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saque(conta, valor):
    conta["saldo"] -= valor 

def extrato(conta):
    print("O seu salde é de R${}" .format(conta["saldo"]))

conta = cria_conta(123,"Vini", 150.0, 1050.0)

deposita(conta, 200)
extrato(conta)

saque(conta, 20)
extrato(conta)