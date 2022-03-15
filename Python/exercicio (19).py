def printLetra(a):
    for letra in a:
        print(letra)
frase = input('')
printLetra(frase)
def divFrase(a):
    a = a.split(' ')
    a = (f'{a[0]} {a[-1]}')
    return a
frase = input('')
print(divFrase(frase))
