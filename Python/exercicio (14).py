condicao = ""
logica = []
email = ""
i = 0
x = 0
while email != "sair":
    email = input()
    lista = list(email)
    if email != "sair":
        if lista.count(".") == 2 and lista.count("@") == 1 and lista.index("@") > 0 and lista[lista.index("@") + 1] != "." and lista[lista.index(".") + 1] != "." and lista[-1] != ".":
            logica.append("certo")
        else:
            logica.append("errado")
    else:
        break
    i = i + 1

while x < i:
    print(logica[x])
    x = x + 1