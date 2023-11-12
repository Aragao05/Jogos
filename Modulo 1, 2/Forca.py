#jogo da forca


def jogar():

    print("################################")
    print("## Bem vindo ao jogo da forca ##")
    print("################################")

    palavra_secreta = "banana".upper()
    letras_acertadas = []

    for i in palavra_secreta:
        letras_acertadas.append("_")
        
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while(not enforcou and not acertou):
        
        chute = input("Qual a letra?:")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            posiçao = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[posiçao] = letra
                posiçao += 1
        else:
            tentativas += 1

        acertou = "_" not in letras_acertadas

        enforcou = tentativas == 6

        if (acertou):
            print("Você ganhou!")
        else:
            print("Você perdeu!")

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()