# Jogo do Par ou Ímpar.
from random import randint
barra = '=-' * 17
linha = '-' *30
vitoria = 0
print(f"""{barra}
\tVAMOS JOGAR PAR OU ÍMPAR
{barra}""")
while True:
    jogador = int(input(f"Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input(f"Par ou Ímpar? [P/Í] ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total} ", end='')
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    if tipo == 'P':
        if total % 2 == 0:
            print("Você VENCEU!")
            vitoria += 1
        else:
            print("Você PERDEU!")
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print("Você VENCEU!")
            vitoria += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")
print(f"{barra}\nGAMER OVER! Você venceu {vitoria} vezes.\n{barra}")
