codigo = input()
codigo = codigo.upper()
valorTotal = {}
codigos = []

while codigo != "FIM":
    nome = input()
    valor = float(input())
    quant = int(input())

    valorTotal[codigo] = valor
    codigos.append(codigo)

    codigo = input()
    codigo = codigo.upper()

codigo = input()
codigo = codigo.upper()
aparicoes = []
valoresOrg = {}
valores = {}
i = 0
while codigo != "FIM":
    valor = float(input())

    valorTotal[codigo] = valorTotal[codigo] + valor
    aparicoes.append(codigo)
    if codigo not in valoresOrg:
        valoresOrg[codigo] = f"{valor:.2f}"
    else:
        valoresOrg[codigo] = f"{valoresOrg[codigo]} {f'{valor:.2f}'}"
    valores[f"{aparicoes[i]} {i}"] = f"{valor:.2f}"
    i = i + 1

    codigo = input()
    codigo = codigo.upper()

i = 0
media = {}
while len(codigos) > i:
    media[codigos[i]] = (valorTotal[codigos[i]] / (aparicoes.count(codigos[i]) + 1))
    valoresOrg[codigos[i]] = valoresOrg[codigos[i]].split()
    i = i + 1

i = 0
while len(aparicoes) > i:
    anterior = valoresOrg[aparicoes[i]].index(valores[f"{aparicoes[i]} {i}"])
    if anterior > 0:
        anteriorDef = anterior - 1
        x = valoresOrg[aparicoes[i]].pop(anteriorDef)
    if float(valores[f"{aparicoes[i]} {i}"]) > media[aparicoes[i]]:
        print("Venda")
    elif anterior > 0:
        if float(valores[f"{aparicoes[i]} {i}"]) > float(x):
            print("Venda")
        else:
            print("Compra")
    else:
        print("Compra")
    i = i + 1