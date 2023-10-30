#Jogo de Adivinhação
import random
def jogar():
    print("################################")
    print("Bem vindo ao jogo de adivinhação")
    print("################################")

    #escolhe o nivel de dificuldade do jogo 
    print("Você quer jogar em que nivel de dificuldade?")
    dificuldade = int(input("Facil (1), Medio (2), Dificil (3)\n"))

    if (dificuldade == 1):
        tentativas = 20
    elif(dificuldade == 2):
        tentativas = 10
    else:
        tentativas = 5
    #escolhe o nivel de dificuldade do jogo


    numero_secreto = random.randrange(0,101) #sortea o numero 
    pontos = 0 #contador de pontos, quanto mais pontos pior 

    # O for serve pra rodar as tentativas 
    for i in range(0,tentativas):
        rodada = i + 1
        print("Tentativa numero {} de {}".format(rodada,tentativas))
        print("Digite um numero entre 1 e 100")
        chute = int(input("Digite o numero:"))

        # saber se o jogador acertou ou errou o numero
        acertou = chute == numero_secreto
        menor = chute > numero_secreto
        maior = chute < numero_secreto

        #caso digite um numero maior ou menor que o permitido exibe a mensagem
        if (chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100")
            continue
        
        #se acertou entra nesse
        if (acertou):
            print("Parebens voce acertou o numero sorteado")
            break
        # se errou entra nesse que exibe por jogador se o numero digitado é 
        # maior ou menor que o numero sorteado 
        else:
            if (menor):
                print("\nVoce errou, o numero é menor\n")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos + pontos_perdidos
            elif(maior):
                print("\nVoce errou, o numero é maior\n")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos + pontos_perdidos
        # saber se o jogador acertou ou errou o numero

    print(f"Você fez {pontos} pontos")
    print(f"Fim do jogo o numero sorteado era:{numero_secreto}")

#executa o jogo pelo terminal e pelo ide sem falha 
if(__name__ == "__main__"):
    jogar()