# Estatísticas em produtos.
barra = '-' * 13
print(f"{barra+barra}\n\tLOJA SUPER BARATÃO\n{barra+barra}")
precoTotal = maiorMil = 0
produtoMenor = ''
precoMenor = contador = 0
while True:
    nome = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))
    precoTotal += preco
    contador += 1
    if preco > 1000:
        maiorMil += 1
    if contador == 1:
        precoMenor = preco
        produtoMenor = nome
    else:
        if preco < precoMenor:
            precoMenor = preco
            produtoMenor = nome
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == 'N':
            break
print(f"{barra} FIM DO PROGRAMA {barra}")
print(f"O total de compra foi de R${precoTotal}")
print(f"Temos {maiorMil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {produtoMenor} que custa R${precoMenor:.2f}")
