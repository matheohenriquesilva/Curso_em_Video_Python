# Maior e Menor valores na Lista.
valores = list()        # []
maior = menor = 0
for casa in range(0, 5):
    valores.append(int(input(f"Digite um valor para posição {casa}: ")))
    if casa == 0:
        maior = menor = valores[casa]
    else:
        if valores[casa] > maior:
            maior = valores[casa]
        if valores[casa] < menor:
            menor = valores[casa]
print('=-' * 30)
print("Você digitou os valores", valores)
print(f"O maior valor digitado foi {maior} nas posições ", end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}... ", end='')
print()
print(f"O menor valor digitado foi {menor} nas posições ", end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}... ", end='')
print()
