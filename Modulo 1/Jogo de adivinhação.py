#Jogo de Adivinhação

print("################################")
print("Bem vindo ao jogo de adivinhação")
print("################################")

numero_secreto = 42
tentativas = 3

for i in range(0,tentativas):
    rodada = i + 1
    print("Tentativa numero {} de 3".format(rodada))
    print("Digite um numero entre 1 e 100")
    chute = int(input("Digite o numero:"))

    acertou = chute == numero_secreto
    menor = chute > numero_secreto
    maior = chute < numero_secreto

    if (chute < 1 or chute > 100):
        print("Voce deve digitar um numero entre 1 e 100")
        continue
    
    if (acertou):
        print("Parebens voce acertou o numero sorteado")
        break
    else:
        if (menor):
            print("\nVoce errou, o numero é menor\n")
        elif(maior):
            print("\nVoce errou, o numero é maior\n")
    
print("Fim do jogo")