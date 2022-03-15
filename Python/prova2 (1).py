quantPalavras = int(input())
palavras = []
pesos = []
aparicoes = []

i = 0
while quantPalavras > i:
    palavraPeso = input()
    espaco = palavraPeso.find(" ")
    palavra = palavraPeso[0:espaco]
    palavra = palavra.upper()
    palavras.append(palavra)
    peso = palavraPeso[espaco + 1:]
    pesos.append(peso)
    i = i + 1

limite = float(input())
texto = input()
texto = texto.replace(".", "")
texto = texto.replace(",", "")
texto = texto.upper()

i = 0
while len(palavras) > i:
    aparicoes.append(texto.count(f" {palavras[i]} "))
    i = i + 1

i = 0
pesoFinal = 0
while len(pesos) > i:
    pesoFinal = pesoFinal + float(pesos[i]) * float(aparicoes[i])
    i = i + 1

i = 0
while len(palavras) > i:
    if aparicoes[i] > 0:
        print(f"{palavras[i]} {aparicoes[i]}")
    i = i + 1
if pesoFinal > limite:
    print("SIM")
elif pesoFinal < limite:
    print("NÃO")