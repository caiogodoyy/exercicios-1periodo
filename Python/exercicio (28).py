entrada = input().split()
raca = entrada[0]
raca = raca.upper()
horario_atual = entrada[1]
horario_atual = horario_atual.upper()
tempo_atual = entrada[2]
tempo_atual = tempo_atual.lower()
altura = float(entrada[3])
luta = float(entrada[4])
stealth = float(entrada[5])

#Anao
if raca == "A":
    ser = "anao"
    if altura < 1.50:
        stealth += 2
    if altura > 1.80:
        stealth += -5

#Bruxo
if raca == "B":
    ser = "bruxo"
    if tempo_atual == "c":
        luta += 3
        stealth += 3
    if tempo_atual == "s":
        stealth += -1
    if altura < 1.70:
        stealth += 3
    if altura > 2.00:
        stealth += -4
    if tempo_atual == "n":
        stealth = 10
        luta = 10
    if horario_atual == "D":
        stealth = 0
        luta = 0

#Elfo
if raca == "E":
    ser = "elfo"
    if tempo_atual == "c":
        luta += -2
    if tempo_atual == "s":
        stealth += -1
    if altura < 1.60:
        stealth += 1
    if altura > 1.90:
        stealth += -6
    if tempo_atual == "n":
        stealth = 0
        luta = 0
    if horario_atual == "N":
        stealth = 0
        luta = 0

porcentagem = 10 * ((luta + stealth) / 2)
if raca == "H":
    ser = "humano"
    porcentagem = 100.00

if porcentagem > 100:
    print(f"A taxa de sucesso do {ser} para entrar em Novigrad e de 100.00%")
elif porcentagem < 0:
    print(f"A taxa de sucesso do {ser} para entrar em Novigrad e de 0.00%")
else:
    print(f"A taxa de sucesso do {ser} para entrar em Novigrad e de {porcentagem:.2f}%")