# Valores únicos em uma Lista.
from time import sleep
valores = list()
while True:
    numero = (int(input("Digite um valor: ")))
    sleep(0.3)
    if numero not in valores:
        valores.append(numero)
        print("valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == 'N':
        break
print("-=" * 30)
valores.sort()
print(f"Você digitou os valores {valores}")
