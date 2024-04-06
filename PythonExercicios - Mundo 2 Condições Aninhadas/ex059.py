# Criando um Menu de Opções.
from time import sleep
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print("""\t\t[ 1 ] Somar
    \t[ 2 ] Multiplicar
    \t[ 3 ] Maior
    \t[ 4 ] Novos números
    \t[ 5 ] Sair do programa""")
    opcao = int(input(">>>>> Qual é a sua opção? "))
    if opcao == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} + {n2} é {soma}")
    elif opcao == 2:
        multi = n1 * n2
        print(f"O resultado de {n1} x {n2} é {multi}")
    elif opcao == 3:
        if n1 == n2:
            print(f"Entre {n1} e {n2} os valores são iguais.")
        elif n1 > n2:
            print(f"Entre {n1} e {n2} o maior valor é {n1}")
        else:
            print(f"Entre {n1} e {n2} o maior valor é {n2}")
    elif opcao == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente")
    sleep(1)
    print('=-=' * 10)
print("Fim do programa! Volte sempre!")
