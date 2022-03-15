qnt_colunasElinhas = input()
espaco = qnt_colunasElinhas.find(" ")
qnt_colunas = int(qnt_colunasElinhas[:espaco])
qnt_linhas = int(qnt_colunasElinhas[espaco+1:])

colunas = []
i = 0
while qnt_colunas > i:
    z = i+1
    x = 0
    while qnt_linhas > x:
        colunas.append(z)
        z += qnt_colunas
        x += 1
    i += 1

resposta = []
resposta_dict = {}
i = 0
while i < 3:
    coluna_escolhida = int(input())
    cor_escolhida = input().upper()
    x = 1
    while qnt_colunas >= x:
        if coluna_escolhida == x:
            posicao_lista = (coluna_escolhida - 1) * qnt_linhas
            if cor_escolhida == "R":
                z = 0
                while qnt_linhas > z:
                    resposta.append(colunas[posicao_lista + z])
                    z += 1
            if cor_escolhida == "G":
                z = 0
                while qnt_linhas > z:
                    if colunas[posicao_lista + z] % 2 == 0:
                        resposta.append(colunas[posicao_lista + z])
                    z += 1
            if cor_escolhida == "B":
                z = 0
                while qnt_linhas > z:
                    if colunas[posicao_lista + z] % 2 != 0:
                        resposta.append(colunas[posicao_lista + z])
                    z += 1
            resposta_dict[f"resposta_{i}"] = resposta[0:z]
            resposta.clear()
        x += 1
    i += 1

i = 0
while i < 3:
    x = 0
    print("")
    while len(resposta_dict[f"resposta_{i}"]) > x:
        print(resposta_dict[f"resposta_{i}"][x])
        x += 1
    i += 1