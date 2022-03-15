condicao = "S"
numVeiculosPais = 0
numAcidentesPais = 0
numAcidentes = 0
vitimasFPais = 0
vitimasNFPais = 0
semVitimasPais = 0
acidentesMaior = 0
cidadeMaisAcidentes = ""
acidentesMenor = None
cidadeMenosAcidentes = ""
mediaVeiculos = 0
mediaVitimasF = 0
mediaVitimasNF = 0
mediaSemVitimas = 0
i = 0
maiorIVT = 0
menorIVT = None
cidadeMaiorIVT = ""
cidadeMenorIVT = ""
maiorIVTcidade = ""
maiorIVTnumVeiculos = 0
maiorIVTvitimasF = 0
maiorIVTvitimasNF = 0
maiorIVTsemVitimas = 0
menorIVTcidade = ""
menorIVTnumVeiculos = 0
menorIVTvitimasF = 0
menorIVTvitimasNF = 0
menorIVTsemVitimas = 0

while condicao != "N" and condicao != "n":
    cidade = input()
    numVeiculos = int(input())
    vitimasF = int(input())
    vitimasNF = int(input())
    semVitimas = int(input())

    IVT = (5 * vitimasF + 3 * vitimasNF + semVitimas) / numVeiculos
    numVeiculosPais = numVeiculosPais + numVeiculos
    numAcidentesPais = numAcidentesPais + vitimasF + vitimasNF + semVitimas
    numAcidentes = vitimasF + vitimasNF + semVitimas
    vitimasFPais = vitimasFPais + vitimasF
    vitimasNFPais = vitimasNFPais + vitimasNF
    semVitimasPais = semVitimasPais + semVitimas

    if acidentesMaior < numAcidentes:
        acidentesMaior = numAcidentes
        cidadeMaisAcidentes = cidade

    if acidentesMenor == None:
        acidentesMenor = numAcidentes
        cidadeMenosAcidentes = cidade
    if acidentesMenor > numAcidentes:
        acidentesMenor = numAcidentes
        cidadeMenosAcidentes = cidade

    if maiorIVT < IVT:
        maiorIVT = IVT
        cidadeMaiorIVT = cidade

        maiorIVTcidade = cidade
        maiorIVTnumVeiculos = numVeiculos
        maiorIVTvitimasF = vitimasF
        maiorIVTvitimasNF = vitimasNF
        maiorIVTsemVitimas = semVitimas


    if menorIVT == None:
        menorIVT = IVT
        cidadeMenorIVT = cidade

        menorIVTcidade = cidade
        menorIVTnumVeiculos = numVeiculos
        menorIVTvitimasF = vitimasF
        menorIVTvitimasNF = vitimasNF
        menorIVTsemVitimas = semVitimas
    if menorIVT > IVT:
        menorIVT = IVT
        cidadeMenorIVT = cidade

        menorIVTcidade = cidade
        menorIVTnumVeiculos = numVeiculos
        menorIVTvitimasF = vitimasF
        menorIVTvitimasNF = vitimasNF
        menorIVTsemVitimas = semVitimas

    i = i + 1

    condicao=input()

mediaVeiculos = numVeiculosPais / i
mediaVitimasF = vitimasFPais / i
mediaVitimasNF = vitimasNFPais / i
mediaSemVitimas = semVitimasPais / i

print(f"\n4.a) A quantidade de veículos no país: {numVeiculosPais}")
print(f"4.b) A quantidade de acidentes no país: {numAcidentesPais}")
print(f"4.c) A quantidade de acidentes com vítimas fatais no país: {vitimasFPais}")
print(f"4.d) O município com maior número de acidentes: {cidadeMaisAcidentes} ({acidentesMaior})")
print(f"4.d) O município com menor número de acidentes: {cidadeMenosAcidentes} ({acidentesMenor})")
print(f"\n5.a) A média de veículos por municípios: {mediaVeiculos}")
print(f"5.b) A média de acidentes com vítimas fatais por municípios: {mediaVitimasF}")
print(f"5.b) A média de acidentes com vítimas não-fatais por municípios: {mediaVitimasNF}")
print(f"5.b) A média de acidentes sem vítimas por municípios: {mediaSemVitimas}")
print(f"\n5.c) O maior IVT é de {maiorIVT} e pertence ao município {maiorIVTcidade}")
print(f"5.d) Nome do município: {maiorIVTcidade}")
print(f"5.d) Quantidade de veículos de {maiorIVTcidade}: {maiorIVTnumVeiculos}")
print(f"5.d) Total de acidentes com vítimas fatais em {maiorIVTcidade}: {maiorIVTvitimasF}")
print(f"5.d) Total de acidentes com vítimas não-fatais em {maiorIVTcidade}: {maiorIVTvitimasNF}")
print(f"5.d) Total de acidentes sem vítimas em {maiorIVTcidade}: {maiorIVTsemVitimas}")
print(f"\n5.c) O menor IVT é de {menorIVT} e pertence ao município {menorIVTcidade}")
print(f"5.d) Nome do município: {menorIVTcidade}")
print(f"5.d) Quantidade de veículos de {menorIVTcidade}: {menorIVTnumVeiculos}")
print(f"5.d) Total de acidentes com vítimas fatais em {menorIVTcidade}: {menorIVTvitimasF}")
print(f"5.d) Total de acidentes com vítimas não-fatais em {menorIVTcidade}: {menorIVTvitimasNF}")
print(f"5.d) Total de acidentes sem vítimas em {menorIVTcidade}: {menorIVTsemVitimas}")