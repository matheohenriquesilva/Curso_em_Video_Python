# Exercício Python #081 - Extraindo dados de uma Lista.
elementos = 0
lista = []
while True:
    valor = int(input("Digite um valor: "))
    elementos += 1
    lista.append(valor)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == 'N':
        break
#
lista.sort(reverse=True)
print('-=' * 50)
print(f"Você digitou {elementos} elementos.")
print(f"Os valores em ordem decrescente são {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")
