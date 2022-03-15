cardapio = {}
numProdutos = int(input())
pedido = None
i = 0
while numProdutos > i:
    LED = int(input())
    descricao = input()
    preco = float(input())
    cardapio[f"LED{i}"] = LED
    cardapio[f"descricao{i}"] = descricao
    cardapio[f"preco{i}"] = preco

    i = i + 1

i = 0
pedido = int(input())
while pedido != 0:
    quant = int(input())
    if quant < 0:
        quant = 0
    cardapio[f"pedido{i}"] = pedido
    cardapio[f"quant{i}"] = quant
    i = i + 1
    pedido = int(input())

quantpedidos = i

x = 0
valor = 0.00
while numProdutos > x:
    i = 0
    while quantpedidos > i:
        if cardapio[f"pedido{i}"] == cardapio[f"LED{x}"]:
            valor = valor + cardapio[f"preco{x}"] * cardapio[f"quant{i}"]
        i = i + 1
    x = x + 1

print(f"{valor:5.2f}")