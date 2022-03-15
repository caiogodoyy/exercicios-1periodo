quantPalavras = int(input())
pesoProibidas = {}
palavrasProibidas = []
contagem = {}

i = 0
while quantPalavras > i:
    entrada = input()
    espaco = entrada.find(" ")
    entrada = entrada.upper()
    palavra = entrada[:espaco]
    peso = float(entrada[espaco+1:])
    pesoProibidas[palavra] = peso
    palavrasProibidas.append(palavra)
    i = i + 1

threshold = int(input())
texto = input()
texto = texto.upper()
texto = texto.replace(".", " ")
texto = texto.replace(",", " ")

palavras = texto.split()
for x in palavras:
    contagem[x] = contagem.get(x, 0) + 1

i = 0
total = 0
while len(palavrasProibidas) > i:
    if palavrasProibidas[i] in contagem:
        print(f"{palavrasProibidas[i]} {contagem[palavrasProibidas[i]]}")
        total = total + pesoProibidas[palavrasProibidas[i]] * contagem[palavrasProibidas[i]]
    i = i + 1
if total > threshold:
    print("SIM")
else:
    print("NAO")