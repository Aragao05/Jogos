import random
from time import sleep

alfabeto = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ")

frase = "hello world"
frase_lista = list("hello world")
frase_impressa = []
contador = 0

while frase != frase_impressa:
    aleatorio = random.choice(alfabeto)
    for i in frase_lista:
        if i == frase_lista[contador]:
            frase_impressa[contador] = frase[contador]
            contador += 1

        print(frase_impressa)
