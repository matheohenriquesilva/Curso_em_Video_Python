# Listas com pares e ímpares.
valores = [[], []]
for valor in range(1, 8):
    num = int(input(f"Digite o {valor}º. valor: "))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print('-=' * 50)
print("Os valores pares digitados foram:", valores[0])
print("Os valores ímpares digitados foram:", valores[1])
