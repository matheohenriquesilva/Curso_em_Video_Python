# Análise de dados em uma Tupla.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))
valores = (n1, n2, n3, n4)
cont9 = contPar = 0
for num in valores:
    if num == 9:
        cont9 += 1
    if num % 2 == 0:
        contPar += 1
print(f"Você digitou os valores {valores}")
print(f"O valor 9 apareceu {cont9} vezes")
#print(num.count(9))
if 3 in valores:
    print(f"O valor 3 apareceu na {valores.index(3)+1}ª posição")
else:
    print("O valaor 3 não foi digitado em nenhuma posição")
print(f"Os valores pares foram {contPar}")
