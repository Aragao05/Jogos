import Adivinhação
import Forca

print("################################")
print("###### Escolha o seu jogo ######")
print("################################")

print("(1) Forca (2) Adivinhação")
escolha = int(input("Qual jogo quer jogar ?\n"))

if (escolha == 1):
    print("Jogando Forca")
    Forca.jogar()
elif(escolha == 2):
    print("Jogando Adivinhação")
    Adivinhação.jogar()

