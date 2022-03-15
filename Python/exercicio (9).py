musica = input()
quantSenhas = int(input())

musica = musica.title()

musica = musica.replace("a", "@")
musica = musica.replace("E", "%")
musica = musica.replace("e", "!")
musica = musica.replace("i", "@")
musica = musica.replace("o", "#")
musica = musica.replace("u", "$")

tamanho = len(musica)
musica = musica.replace(" ", "")

vezes = 0
finais = []
usuarios = []
condicoes = []
while quantSenhas > vezes:
    num = int(input())
    while num < 6 or num > tamanho:
        num = int(input())

    condicao = input()
    condicao = condicao.lower()
    condicoes.append(condicao)

    while condicao == "n":
        final = musica[num:]
        finais.append(final[:5])
        num = int(input())
        while num < 6 or num > tamanho:
            num = int(input())
        condicao = input()
        condicao = condicao.lower()
        condicoes.append(condicao)

    usuarios.append(input())

    inicias = []
    i = 0
    x = 0
    while int(len(musica) / 5) > i:
        inicias.append(musica[x:x + 5])
        i = i + 1
        x = x + 1

    final = musica[num:]
    finais.append(final[:5])

    vezes = vezes + 1

meio = musica[-5:]

i = 0
senhas = []
while len(condicoes) > i:
    if condicoes[i-1] == "n":
        senha = inicias[x] + meio + finais[i]
        senhas.append(senha[::-1])
    else:
        senha = inicias[i] + meio + finais[i]
        senhas.append(senha[::-1])
        x = i
    i = i + 1

senhasUser = {}
i = 0
x = 0
while len(condicoes) > i:
    if condicoes[i] == "s":
        senhasUser[usuarios[x]] = senhas[i]
        x = x + 1
    i = i + 1

i = 0
while len(senhas) > i:
    print(senhas[i])
    i = i + 1
print(senhasUser)