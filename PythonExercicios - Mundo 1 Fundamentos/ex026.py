# Primeira e última ocorrência de uma string.
frase = str(input("Digite uma frase: ")).upper().split()
print("A letra A aparece {} vezes na frase.".format(frase.count('A')))
print("A primeira letra A aparece na posição", frase.find('A')+1)
print("A última letra A apareceu na posição", frase.rfind('A')+1)
