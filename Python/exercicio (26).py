modulos = int(input())
numAlunos = int(input())
dadosModulo = {}
dadosListas = {}
nomes = []
notaFinal = []
numListas = []
medias = {}
mediaFinal = []
i = 0
while i < numAlunos:
    nome = input()
    if nome not in nomes:
        nomes.append(nome)
    i = i + 1
i = 0
while i < modulos:
    numListas.append(int(input()))
    y = 0
    while y < numAlunos:
        notaModulo = float(input())
        dadosModulo[f"{nomes[y]}{i}"] = notaModulo
        dadosListas[f"{nomes[y]}{i}"] = 0
        x = 0
        somaAluno = 0
        while x < numListas[i]:
            notaLista = float(input())
            dadosListas[f"{nomes[y]}{i}"] = dadosListas[f"{nomes[y]}{i}"] + float(notaLista)
            x = x + 1
        y = y + 1
    i = i + 1

i = 0
while i < modulos:
    ModuloTotal = 0
    ListasTotal = 0
    y = 0
    while y < numAlunos:
        ModuloTotal = ModuloTotal + dadosModulo[f"{nomes[y]}{i}"]
        ListasTotal = ListasTotal + (dadosListas[f"{nomes[y]}{i}"] / numListas[i])
        y = y + 1
        mediaModuloTotal = ModuloTotal / numAlunos
        mediaListasTotal = ListasTotal / numAlunos
    print(f"{i+1} {(mediaModuloTotal * 0.7) + (mediaListasTotal * 0.3):.2f}")
    i = i + 1

y = 0
while y < numAlunos:
    i = 0
    while i < modulos:
        medias[f"{nomes[y]}{i}"] = f"{((dadosModulo[f'{nomes[y]}{i}'] * 70) + ((dadosListas[f'{nomes[y]}{i}'] / numListas[i]) * 30)) / 100}"
        i = i + 1
    y = y + 1

y = 0
while y < numAlunos:
    i = 0
    mediaFinal_ = 0
    while i < modulos:
        mediaFinal_ = mediaFinal_ + float(medias[f"{nomes[y]}{i}"])
        i = i + 1
    mediaFinal.append(mediaFinal_ / modulos)
    y = y + 1

y = 0
while y < numAlunos:
    i = 0
    if mediaFinal[y] >= 0 and mediaFinal[y] < 3:
        variante = "REPROVADO"
    if mediaFinal[y] >= 3 and mediaFinal[y] < 5:
        variante = "TA DIFICIL"
    if mediaFinal[y] >= 5 and mediaFinal[y] < 7:
        variante = "FOI POR POUCO"
    if mediaFinal[y] >= 7 and mediaFinal[y] < 9:
        variante = "PASSOU"
    if mediaFinal[y] >= 9:
        variante = "PASSOU FACIL"
    print(f"{nomes[y]} {mediaFinal[y]:.2f} {variante}")
    while i < modulos:
        print(f"{i + 1} {float(medias[f'{nomes[y]}{i}']):.2f}")
        i = i + 1
    y = y + 1