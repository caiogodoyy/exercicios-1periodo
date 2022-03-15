entrada = input()
postos = {}
medicoes = []
nomePostos = []
numPostos = []

x = 1
i = 0
while entrada != "FIM":
    espaco = entrada.find(" ")
    espaco2 = entrada.find(" ", espaco+1)
    odometro = int(entrada[0:espaco])
    volume = float(entrada[espaco+1:espaco2])
    posto = entrada[espaco2+1:]

    if posto not in nomePostos:
        nomePostos.append(posto)
    numPostos.append(posto)

    medicoes.append(odometro), medicoes.append(volume)
    if posto in postos:
        if x > 1:
            postos[postoanterior] = postos[postoanterior] + ((medicoes[i+2] - medicoes[i]) / medicoes[i+3])
            i = i + 2
    else:
        postos[posto] = 0
        if x > 1:
            postos[postoanterior] = postos[postoanterior] + ((medicoes[i+2] - medicoes[i]) / medicoes[i+3])
            i = i + 2
    x = x + 1
    postoanterior = posto

    entrada = input()

nomePostos = sorted(nomePostos)
numPostos.pop(-1)
i = 0
while len(postos) > i:
    print(f"{nomePostos[i]}: {postos[nomePostos[i]] / int(numPostos.count(nomePostos[i])):.2f}")
    i = i + 1