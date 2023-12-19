#jogo da forca
import random

#Função que escolhe e retorna a palavra a ser adivinhada pelo jogador 
def SortearPalavra():
    arquivo = open("Palavras.txt","r")
    conteudo = arquivo.read()
    palavras = conteudo.split()
    palavra_secreta = random.choice(palavras).upper()
    arquivo.close()
    return palavra_secreta

#Função que mostra a mensagem de boas vindas ao jogo
def imprime_recepção():
    print("################################")
    print("## Bem vindo ao jogo da forca ##")
    print("################################")

#função que mostra a mensagem de vitoria
def imprime_mensagem_vencedor(palavra_secreta):
    print("Parabéns, você ganhou!")
    print(f"A palavra era {palavra_secreta}")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

#Função que mostra a mensagem de derrota
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

#Função que desenha a forca com o numero de erros 
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |       O   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |       O   ")
        print(" |      /     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |       O   ")
        print(" |      /|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |       O   ")
        print(" |      /|\   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |       O   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |       O   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |       O   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         \n")

#Função que executa o jogo 
def jogar():
    letras_acertadas = []
    letras_digitadas = []
    imprime_recepção()
    palavra_secreta = SortearPalavra()

    #cria a as linhas em baixo de cada palavra
    for i in palavra_secreta:
        letras_acertadas.append("_") #.append adiciona algo no fim de uma lista
        
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    #laço que confere se o jogador acertou a palavra 
    while(not enforcou and not acertou):
        
        chute = input("Qual a letra?:")
        chute = chute.strip().upper() #.strip() remove algo da string, no caso se tiver algum espaço, ,upper deixa a string toda em maiusculo
        letras_digitadas.append(chute)

        #Confere se o digitou uma letra que contem na palavra
        #se acertou coloca a letra na lista que contem a palavra salva
        if chute in palavra_secreta:
            posiçao = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[posiçao] = letra
                posiçao += 1
        #se errou soma mais um para o numero de erros quando errar 7 acaba o jogo 
        else:
            tentativas += 1

        acertou = "_" not in letras_acertadas 
        enforcou = tentativas == 7
        print(letras_acertadas)
        print(f"Letras digitadas:\n{letras_digitadas}")
        desenha_forca(tentativas)

    #Confere se o jogador acertou ou não a palavra e imprime a mensagem de 
    #vitoria ou de derrota
    if (acertou):
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim do jogo")

#Executa o jogo tanto terminal como na IDE
if(__name__ == "__main__"):
    jogar()