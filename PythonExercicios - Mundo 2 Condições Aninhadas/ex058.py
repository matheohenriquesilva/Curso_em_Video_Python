# (Jogo da Adivinhação v2.0).
from random import randint
print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi?""")
computador = randint(0, 10)
contador = 0
palpite = 0
while palpite != computador:
    palpite = int(input("Qual é seu palpite? "))
    contador += 1
    if computador > palpite:
        print("Mais... Tente mais uma vez.")
    if computador < palpite:
        print("Menos... Tente mais uma vez.")
print(f"Acertou com {contador} tentativas. Parabéns!")
