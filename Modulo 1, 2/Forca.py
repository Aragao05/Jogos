#jogo da forca


def jogar():

    print("################################")
    print("## Bem vindo ao jogo da forca ##")
    print("################################")

    palavra_secreta = "banana"
    letras_acertadas = []

    for i in palavra_secreta:
        letras_acertadas.append("_")
        
    print(letras_acertadas)

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        
        chute = input("Qual a letra?:")
        chute = chute.strip()

        posiçao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posiçao] = letra
            posiçao += 1

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()