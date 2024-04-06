# Números Primos.
numero = int(input("Digite um número: "))
total = 0
for c in range(1, numero + 1):
    if numero % c == 00:
        print('\033[31m', end=' ')
        total += 1
    else:
        print('\033[36m', end=' ')
    print(f"{c}", end=' ')
print(f"\n\033[mO número {numero} foi divisivel {total} vezes")
if total == 2:
    print("Por isso ele é PRIMO")
else:
    print("Por isso ele NÃO É PRIMO")
