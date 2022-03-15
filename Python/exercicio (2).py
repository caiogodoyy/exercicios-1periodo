alimentos = {}
peso = []
pesototal = []
testes = []
a = 0
alimento = input()
while alimento != "*":
    virgula = alimento.find(",")
    nome = alimento[0:virgula]
    num = alimento[virgula + 1:]
    alimentos[f"nome{a}"] = nome
    alimentos[f"num{a}"] = num
    a = a + 1
    alimento = input()

z = 0
i = 0
quantsaidas = 0
testestotal = 0
teste = int(input())
while teste > 0:
    testes.append(teste)
    testestotal = testestotal + teste
    z = 0
    x = 0
    peso.clear()
    while teste > z:
        x = 0
        quant = input()
        espaco = quant.find(" ")
        nomeT = quant[espaco+1:]
        numT = quant[0:espaco]
        alimentos[f"nomeT{i}"] = nomeT
        alimentos[f"numT{i}"] = numT
        while a > x:
            if alimentos[f"nomeT{i}"] == alimentos[f"nome{x}"]:
                peso.append(int(alimentos[f"num{x}"]) * int(alimentos[f"numT{i}"]))
            x = x + 1
        i = i + 1
        z = z + 1
    pesototal.append(sum(peso))
    teste = int(input())

i = 0
while len(pesototal) > i:
    if pesototal[i] > 130:
        print(f"Menos {pesototal[i] - 130} mg")
    if pesototal[i] < 110:
        print(f"Mais {110 - pesototal[i]} mg")
    if pesototal[i] > 110 and pesototal[i] < 130:
        print(f"{pesototal[i]} mg")
    i = i + 1