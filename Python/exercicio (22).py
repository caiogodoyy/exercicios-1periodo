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

print(f"\n4.a) A quantidade de ve??culos no pa??s: {numVeiculosPais}")
print(f"4.b) A quantidade de acidentes no pa??s: {numAcidentesPais}")
print(f"4.c) A quantidade de acidentes com v??timas fatais no pa??s: {vitimasFPais}")
print(f"4.d) O munic??pio com maior n??mero de acidentes: {cidadeMaisAcidentes} ({acidentesMaior})")
print(f"4.d) O munic??pio com menor n??mero de acidentes: {cidadeMenosAcidentes} ({acidentesMenor})")
print(f"\n5.a) A m??dia de ve??culos por munic??pios: {mediaVeiculos}")
print(f"5.b) A m??dia de acidentes com v??timas fatais por munic??pios: {mediaVitimasF}")
print(f"5.b) A m??dia de acidentes com v??timas n??o-fatais por munic??pios: {mediaVitimasNF}")
print(f"5.b) A m??dia de acidentes sem v??timas por munic??pios: {mediaSemVitimas}")
print(f"\n5.c) O maior IVT ?? de {maiorIVT} e pertence ao munic??pio {maiorIVTcidade}")
print(f"5.d) Nome do munic??pio: {maiorIVTcidade}")
print(f"5.d) Quantidade de ve??culos de {maiorIVTcidade}: {maiorIVTnumVeiculos}")
print(f"5.d) Total de acidentes com v??timas fatais em {maiorIVTcidade}: {maiorIVTvitimasF}")
print(f"5.d) Total de acidentes com v??timas n??o-fatais em {maiorIVTcidade}: {maiorIVTvitimasNF}")
print(f"5.d) Total de acidentes sem v??timas em {maiorIVTcidade}: {maiorIVTsemVitimas}")
print(f"\n5.c) O menor IVT ?? de {menorIVT} e pertence ao munic??pio {menorIVTcidade}")
print(f"5.d) Nome do munic??pio: {menorIVTcidade}")
print(f"5.d) Quantidade de ve??culos de {menorIVTcidade}: {menorIVTnumVeiculos}")
print(f"5.d) Total de acidentes com v??timas fatais em {menorIVTcidade}: {menorIVTvitimasF}")
print(f"5.d) Total de acidentes com v??timas n??o-fatais em {menorIVTcidade}: {menorIVTvitimasNF}")
print(f"5.d) Total de acidentes sem v??timas em {menorIVTcidade}: {menorIVTsemVitimas}")