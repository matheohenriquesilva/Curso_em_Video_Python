# Conversor de Bases Númericas.
num = int(input("Digite um número inteiro: "))
print("""Escolha umas das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("{} em decimal é {} em BINÁRIO.".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} em decimal é {} em OCTAL.".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} em decimal é {} em HEXADECIMAL.".format(num, hex(num)[2:]))
else:
    print("OPÇÃO INVALIDA!")
