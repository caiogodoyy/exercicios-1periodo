entrada = input().lower()

mesa1 = []
mesa2 = []
mesa3 = []
mesa4 = []

i = 0
while entrada != "-1":
    entrada = entrada.split()
    nome = entrada[0]
    nome = nome.upper()
    idade = int(entrada[1])
    time = entrada[2]

    if (time == "flamengo" or time == "sport" or time == "vitoria") and idade >= 30:
        mesa1.append(nome)
    elif (time == "vasco" or time == "treze" or time == "santos") and (idade >= 18 and idade <= 36):
        mesa2.append(nome)
    elif (time == "bahia" or time == "fortaleza" or time == "gremio") and (idade > 10 and idade < 18):
        mesa3.append(nome)
    else:
        mesa4.append(nome)
    i += 1
    if i == 10:
        break
    entrada = input().lower()

if i == 0:
    print("JANTAR SEM CONVIDADOS")
else:
    print("MESA 1")
    if len(mesa1) == 0:
        print("VAZIA")
    else:
        i = 0
        while len(mesa1) > i:
            print(f"{i+1} {mesa1[i]}")
            i += 1
    print("\nMESA 2")
    if len(mesa2) == 0:
        print("VAZIA")
    else:
        i = 0
        while len(mesa2) > i:
            print(f"{i+1} {mesa2[i]}")
            i += 1
    print("\nMESA 3")
    if len(mesa3) == 0:
        print("VAZIA")
    else:
        i = 0
        while len(mesa3) > i:
            print(f"{i+1} {mesa3[i]}")
            i += 1
    print("\nMESA 4")
    if len(mesa4) == 0:
        print("VAZIA")
    else:
        i = 0
        while len(mesa4) > i:
            print(f"{i+1} {mesa4[i]}")
            i += 1