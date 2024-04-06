# Lista composta e análise de dados.
galera = list()
pessoa = list()
contador = maiorP = menorP = 0
while True:
    pessoa.append(str(input("Nome: ")))
    pessoa.append(float(input("Peso: ")))
    if len(galera) == 0:
        maiorP = menorP = pessoa[1]
    else:
        if pessoa[1] > maiorP:
            maiorP = pessoa[1]
        if pessoa[1] <menorP:
            menorP = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()
    contador += 1
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input("Quer continuar? [S/N] ")).strip()[0]
    if opcao in 'Nn':
        break
print('-=' * 50)
print(f"Ao todo, você cadastrou {contador} pessoas.")
print(f"O maior peso foi de {maiorP}Kg. Peso de ", end='')
for p in galera:
    if p[1] == maiorP:
        print(f"[{p[0]}]", end=' ')
print()
print(f"O menor peso foi de {menorP}Kg. ", end='')
for p in galera:
    if p[1] == menorP:
        print(f"[{p[0]}] ", end='')
print()
