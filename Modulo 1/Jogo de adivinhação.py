#Jogo de Adivinhação

print("################################")
print("Bem vindo ao jogo de adivinhação")
print("################################")

numero_secreto = 42
tentativas = 1

while (tentativas < 4):
    print("Tentativa numero {} de 3".format(tentativas))
    chute = int(input("Digite o numero:"))

    acertou = chute == numero_secreto
    menor = chute > numero_secreto
    maior = chute < numero_secreto
    
    if (acertou):
        print("Parebens voce acertou o numero sorteado")
        break
    else:
        if (menor):
            print("Voce errou, o numero é menor")
        elif(maior):
            print("Voce errou, o numero é maior")

    tentativas += 1