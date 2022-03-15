frase = input("Digite uma frase: ")
palavra = input("Agora uma palavra que pode, ou não, estar dentro da frase: ")

frasenova = frase.replace(palavra,"Domingo")

if (frasenova == frase):
    print("Não houve modificação na frase! A frase permanece ",frase)
else:
    print("Houve modificação na frase! A nova frase é ",frasenova)