quantLista = input()
doacao = float(input())
quantLista = quantLista.replace(","," ")
quantLista = quantLista.split()

produtos = []
produtos.append(5.50)
produtos.append(6.00)
produtos.append(7.50)
produtos.append(1.99)
produtos.append(4.00)
produtos.append(6.70)
produtos.append(1.20)
produtos.append(2.80)
produtos.append(5.30)
produtos.append(5.00)
produtos.append(3.00)
produtos.append(2.00)
produtos.append(3.50)
produtos.append(0.80)
produtos.append(1.00)
produtos.append(0.80)
produtos.append(5.40)
produtos.append(1.90)
produtos.append(5.00)
produtos.append(10.00)
produtos.append(0.50)
produtos.append(0.50)
produtos.append(5.00)
produtos.append(4.50)
produtos.append(1.99)
produtos.append(2.90)
produtos.append(0.30)

i = 0
valorTotal = 0
while len(quantLista) > i:
    valorTotal = valorTotal + int(quantLista[i]) * produtos[i]
    i = i + 1

print(f"O valor da cesta básica ficou em: R${valorTotal:.2f}")
print(f"Com o valor doado pode ser comprada {int(doacao / valorTotal)} cestas básicas")