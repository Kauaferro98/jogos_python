import forca
import adivinhacao
print("*********************************")
print("Escolha o seu jogo!!")
print("*********************************")

print("(1) Forca (2) Advinhação")

jogo = int (input("Qual JOgo?"))

if (jogo == 1):
    print("jogando Forca")
    forca.jogar_forca()

elif (jogo == 2):
    print("jogando Adivinhação")
    adivinhacao.jogar_adivinhacao()