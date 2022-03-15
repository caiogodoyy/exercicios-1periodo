frase1 = input()
frase2 = input()

frase1 = frase1.upper()
frase2 = frase2.upper()

frase1 = frase1.replace(" ", "")
frase2 = frase2.replace(" ", "")
frase1 = frase1.replace(".", "")
frase2 = frase2.replace(".", "")
frase1 = frase1.replace(",", "")
frase2 = frase2.replace(",", "")
frase1 = frase1.replace("!", "")
frase2 = frase2.replace("!", "")
frase1 = frase1.replace("?", "")
frase2 = frase2.replace("?", "")

lista1 = list(frase1)
lista2 = list(frase2)
lista1.sort()
lista2.sort()

if lista1 == lista2:
    print("True")
else:
    print("False")