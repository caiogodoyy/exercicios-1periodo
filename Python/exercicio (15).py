tamanho = int(input())
listaFrase = []
listaBase = []
resp = []
i = 0
x = 0

while tamanho > 0:
    frase = input()
    listaFrase.append(frase)
    tamanho = tamanho - 1

base = input()
listaBase = list(base)

loop = len(listaBase)
loop2 = len(listaFrase)

while loop > i:
    resp.append(0)
    x = 0
    while loop2 > x:
        resp[i] = resp[i] + listaFrase[x].count(listaBase[i])
        x = x + 1
    i = i + 1

i = 0
while i < loop:
    print(listaBase[i], "=", resp[i])
    i = i + 1