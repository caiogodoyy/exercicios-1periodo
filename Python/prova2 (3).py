modulos = int(input())
alunos = int(input())
biblioteca = {}
i = 0
while alunos > i:
    biblioteca[f"nomeAluno{i}"] = input()
    i = i + 1
i = 0
x = 0
while modulos > x:
    i = 0
    while alunos > i:
        quantListas = int(input())
        biblioteca[f"quantListas{i}"] = quantListas
        notaAvaliacao = float(input())
        biblioteca[f"notaAvaliacao{i}"] = notaAvaliacao
        while quantListas > i:
            notasListas = float(input())
            biblioteca[f"notasListas{i}"] = notasListas
            i = i + 1
        x = x + 1

y = 0
i = 0
while modulos > y:
    x = 0
    while biblioteca[f"quantListas{y}"] > i:
        x = x + biblioteca[f"notasListas{i}"]
        i = i + 1
    biblioteca[f"mediaListas{y}"] = x / biblioteca[f"quantListas{y}"]
    biblioteca[f"notaFinal{y}"] = (biblioteca[f"notaAvaliacao{y}"] * 70 + biblioteca[f"mediaListas{y}"] * 30) / 100
    y = y + 1

i = 0
while alunos > i:
    x = x + biblioteca[f"notaFinal{i}"]
    i = i + 1
i = 0
while modulos > i:
    biblioteca[f"mediaFinalTotal{i}"] = x / alunos
    i = i + 1

i = 0
x = 1
while modulos > i:
    print(x," ", biblioteca[f"mediaFinalTotal{i}"])
    i = i + 1
    x = x + 1
#Sem Tempo