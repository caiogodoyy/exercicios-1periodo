kidsdead = int(input())
if kidsdead <= 0:
    print("Informe um número positivo")

i = kidsdead
meninos = 0
meninas = 0
youngkids = 0

while i > 0:
    sexo = input()
    vida = int(input())

    if sexo == "M" or sexo == "m":
        meninos=meninos+1
    if sexo == "F" or sexo == "f":
        meninas = meninas+1
    if vida <= 24:
        youngkids = youngkids+1

    i = i-1

if kidsdead > 0:
        print(f"a) {(meninas / kidsdead) * 100}% das crianças eram do sexo feminino.")
        print(f"b) {(meninos / kidsdead) * 100}% das crianças eram do sexo masculino.")
        print(f"c) {(youngkids / kidsdead) * 100}% das crianças viveram 24 meses ou menos.")
