# Dividindo valores em várias listas.
lista = []
impares = []
pares = []
while True:
    lista.append(int(input("Digite um número: ")))
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input("Quer continuar? [S/N] "))[0]
    if opcao in 'Nn':
        break
#
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
#
print('-=' * 50)
print("A lista completa é", lista)
print("A lista de pares é", pares)
print("A lista de ímpares é", impares)
