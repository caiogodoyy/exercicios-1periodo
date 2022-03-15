presentes = {}

entrada = input()
while entrada != "*":
    espaco = entrada.rfind(" ")
    presente = entrada[0:espaco]
    valor = float(entrada[espaco+1:])
    presentes[presente] = valor
    entrada = input()

entrada = input()
while entrada != "total":
    if entrada == "quantidade":
        print(len(presentes))
    espaco = entrada.find(" ")
    if entrada[0:espaco] == "retire":
        presentes.pop(entrada[espaco+1:])
    entrada = input()

print(f"{sum(list(presentes.values())):.2f}")