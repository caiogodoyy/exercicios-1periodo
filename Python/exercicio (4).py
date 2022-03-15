entrada = input()
valores = {}
pontos = {}
lista = []
while entrada != "*":
    espaco1 = entrada.find(" ")
    espaco2 = entrada.find(" ", espaco1+1)
    codigo = entrada[0:espaco1]
    valor = entrada[espaco1+1:espaco2]
    ponto = entrada[espaco2+1:]
    valores[codigo] = valor
    pontos[codigo] = ponto
    entrada = input()

entrada = input()
while entrada != "*":
    lista.append(entrada)
    lista = sorted(lista)
    entrada = input()

x = 0
while len(lista) > x:
    espaco = lista[x].find(" ")
    placa = lista[x][0:espaco]
    lista[x] = lista[x][espaco+1:]
    multas = lista[x].split()
    somaValores = 0
    somaPontos = 0
    i = 0
    while len(multas) > i:
        somaValores = somaValores + float(valores[multas[i]])
        somaPontos = somaPontos + int(pontos[multas[i]])
        i = i + 1
    print(f"{placa} {somaValores:.2f} {somaPontos}")
    x = x + 1