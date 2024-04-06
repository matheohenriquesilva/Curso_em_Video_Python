# Maior e menor valores em Tupla.
from random import randint
valores = (randint(0, 11), randint(0, 11), randint(0, 11),
           randint(0, 11), randint(0, 11),)
maior = menor = 0
contador = 0
for num in valores:
    contador += 1
    if num >= maior:
        maior = num
    if contador == 1:
        menor = num
    else:
        if num <= menor:
            menor = num
print(f"Os valores sorteados foram: {valores}")
print(f"O maior valor sorteado foi {maior}")
print(f"O menor valor sorteado foi {menor}")

'''
for n in valores:
    print(f'{n} ', end='')
print(max(valores))         # Maior valor
print(min(valores))         # Menor valor
'''