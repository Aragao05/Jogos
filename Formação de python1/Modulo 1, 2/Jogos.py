import Adivinhação
import Forca

def Escolher_jogo():
    print("################################")
    print("###### Escolha o seu jogo ######")
    print("################################")

    print("\n(1) Forca (2) Adivinhação")
    escolha = int(input("Qual jogo quer jogar ?\n"))

    if (escolha == 1):
        print("Jogando Forca")
        Forca.jogar()
    elif(escolha == 2):
        print("Jogando Adivinhação")
        Adivinhação.jogar()

if(__name__ == "__main__"):
    Escolher_jogo()