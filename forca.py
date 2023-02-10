import random
def jogar_forca():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")
    
    arquivo= open ("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    
    arquivo.close
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].lower() #colocar tudo letra minuscula.
    letras_acertadas = ["_"for letra in palavra_secreta] 

   

    acertou = False
    enforcou = False
    erros = 0

    print (letras_acertadas)

    while (not acertou and not enforcou):
        chute = input("Digite uma letra?")
        chute = chute.strip().lower( ) # tirar o espaço e colocar tudo letra minuscula.
        
        if (chute in palavra_secreta):
            index = 0         
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas [index] = letra
                index += 1       
        else:
            erros += 1       

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas         
        print (letras_acertadas)
            
        
    if (acertou):
        print("Você Ganhou!!!!")
    else:
        print("Você Perdeu !!!!")
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar_forca()