#Jogo de Adivinhação
import random

print("################################")
print("Bem vindo ao jogo de adivinhação")
print("################################")

dificuldade = int(input("Você quer jogar em que nivel de dificuldade?\n Facil (1), Medio (2), Dificil (3)"))

if (dificuldade == 1):
    nivel = 10
    tentativas = 2
elif(dificuldade == 2):
    nivel = 30
    tentativas = 3
else:
    nivel = 50
    tentativas = 5

numero_secreto = random.randrange(0,nivel)

for i in range(0,tentativas):
    rodada = i + 1
    print("Tentativa numero {} de {}".format(rodada,tentativas))
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
    
print(f"Fim do jogo o numero sorteado era:{numero_secreto}")