nome = ""
nomelista = []
resp = []
x = 0
while nome != "*":
    nome = input()
    if nome != "*" and len(nome) < 200:
        nomefinal = []
        i = 0

        nomelista = nome.split()
        loop = len(nomelista)
        while loop > i:
            nomefinal.append(0)
            nomefinal[i] = nomelista[i].capitalize()
            i = i + 1
        nomefinal = " ".join(nomefinal)

        if nomefinal.find(" Da ") >= 0:
            nomefinal = nomefinal.replace("Da","da")
        if nomefinal.find(" De ") >= 0:
            nomefinal = nomefinal.replace("De","de")
        if nomefinal.find(" Di ") >= 0:
            nomefinal = nomefinal.replace("Di","di")
        if nomefinal.find(" Do ") >= 0:
            nomefinal = nomefinal.replace("Do","do")
        if nomefinal.find(" Du ") >= 0:
            nomefinal = nomefinal.replace("Du","du")
        if nomefinal.find(" E ") >= 0:
            nomefinal = nomefinal.replace("E","e")

        resp.append(nomefinal)

if len(nome) < 200:
    i = len(resp)
    while x < i:
        print(resp[x])
        x = x + 1