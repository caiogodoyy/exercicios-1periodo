pessoa1 = input().lower()
pessoa2 = input().lower()
pessoa3 = input().lower()
pessoa4 = input().lower()
pessoa5 = input().lower()

posicao1 = "Princesa"

if pessoa2 == "mario" or pessoa4 == "mario":
    posicao2 = "Mario"
    if pessoa2 == "toad" or pessoa4 == "toad":
        posicao4 = "Toad"
    else:
        posicao3 = "Toad"
if (pessoa2 == "luigi" or pessoa4 == "luigi") and (pessoa2 == "yoshi" or pessoa4 == "yoshi"):
    posicao2 = "Luigi"
    posicao4 = "Yoshi"
elif pessoa2 == "luigi" or pessoa4 == "luigi":
    posicao4 = "Luigi"
    posicao5 = "Yoshi"

if pessoa3 == "mario" or pessoa5 == "mario":
    posicao3 = "Mario"
    if pessoa3 == "toad" or pessoa5 == "toad":
        posicao5 = "Toad"
    else:
        posicao2 = "Toad"
if (pessoa3 == "luigi" or pessoa5 == "luigi") and (pessoa3 == "yoshi" or pessoa5 == "yoshi"):
    posicao3 = "Luigi"
    posicao5 = "Yoshi"
elif pessoa3 == "luigi" or pessoa5 == "luigi":
    posicao5 = "Luigi"
    posicao4 = "Yoshi"

print(posicao1)
print(posicao2)
print(posicao3)
print(posicao4)
print(posicao5)