# Funções aprofundadas em Python.
while True:
    try:
        nI = int(input("Digite um Inteiro: "))
    except (ValueError, TypeError):
        print("\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m")
    else:
        break
#
while True:
    try:
        nR = float(input("Digite um Real: "))
    except (ValueError, TypeError):
        print("\033[0;31mERRO: por favor, digite um número real válido.\033[m")
    else:
        break
#
print(f"O valor inteiro digitado foi {nI} e o real foi {nR}")
