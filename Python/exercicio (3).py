proibidas = input()
proibidas = proibidas.upper()
listaproib = proibidas.split()
listaproib = sorted(listaproib)

texto = {}
i = 0
texto[f"linha{i}"] = ""
while texto[f"linha{i}"] != " FIM ":
    i = i + 1
    texto[f"linha{i}"] = input()
    texto[f"linha{i}"] = texto[f"linha{i}"].replace("."," ")
    texto[f"linha{i}"] = texto[f"linha{i}"].replace(",", " ")
    texto[f"linha{i}"] = texto[f"linha{i}"].upper()
    texto[f"linha{i}"] = " " + texto[f"linha{i}"]
    texto[f"linha{i}"] = texto[f"linha{i}"] + " "

i = 0
listanum = []
while len(listaproib) > i:
    x = 0
    while len(texto) - 1 > x:
        if texto[f"linha{x}"].count(listaproib[i]) > 0:
            listanum.append(0)
            listanum[i] = listanum[i] + texto[f"linha{x}"].count(f" {listaproib[i]} ")
        x = x + 1
    i = i + 1

i = 0
while len(listaproib) > i:
    if listanum[i] > 0:
        print(listaproib[i], listanum[i])
    i = i + 1