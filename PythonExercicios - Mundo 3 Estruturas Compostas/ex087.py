# Mais sobre Matriz em Python.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = maior2l = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = numero = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        if numero % 2 == 0:
            soma += numero
        if coluna == 2:
            soma3 += numero
    if coluna == 0:
        maior2l = numero
    else:
        if linha == 1:
            if numero > maior2l:
                maior2l = numero
print('-=' * 50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^6}]", end='')
    print()
print('-=' * 50)
print("A soma dos valores pares é", soma)
print("A soma dos valores da terceira coluna é", soma3)
print("O maior valor da segunda linha é", maior2l)
