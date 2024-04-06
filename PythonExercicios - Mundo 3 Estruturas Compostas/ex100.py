# Funções para sortear e somar.
from random import randint
def sorteia(lista):
    for i in range(5):
        lista.append(randint(1, 10))
    print(f"Sorteando {len(lista)} valores da lista: ", end='')
    for i in lista:
        print(f"{i} ", end='')
    print("PRONTO!")



def somapar(lista):
    pares = 0
    for i in lista:
        if i % 2 == 0:
            pares += i
    return print(f"Somando os valores pares de {numeros}, temos {pares}")


numeros = list()
sorteia(numeros)
somapar(numeros)
