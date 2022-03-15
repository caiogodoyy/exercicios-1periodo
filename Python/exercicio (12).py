lista = []
palavra = ""
i = 0
x = 1
while palavra != "SAIR" or palavra != "FIM":
    palavra = input()
    palavra = palavra.replace("3", "E")
    palavra = palavra.replace("4", "A")
    palavra = palavra.replace("1", "I")
    palavra = palavra.replace("5", "S")
    palavra = palavra.upper()
    if palavra != "SAIR" or palavra != "FIM":
        lista.append(palavra)
    i = i + 1

while x < i:
    print(lista[x-1])
    x = x + 1