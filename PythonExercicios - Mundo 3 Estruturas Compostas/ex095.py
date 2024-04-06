# Aprimorando os Dicionários.
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do Jogador: "))
    partidas.clear()
    total = int(input(f"Quantas partidas o {jogador['nome']} jogou? "))
    for g in range(0, total):
        partidas.append(int(input(f"\tQuantos gols na partida {g}? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == 'N':
        break
print('-=' * 35)
for k, v in enumerate(time):
    print(f"{k:>4} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print('-=' * 30)
while True:
        prompt = '\nGostaria de mostrar os dados de qual jogador?\n'
        prompt += f'{"(999 para interromper o programa)":^43}'
        # Pergunta o número do jogador para mostrar os dados dele.
        numero = int(input(f'{prompt}\nNúmero: '))
        if numero == 999:
            print(f'\n{"=-=" * 5}\n{"FINALIZANDO..."}\n{"=-=" * 5}')
            break
        elif numero not in range(len(time)):
            print('ERRO! '
                  f'Não existe jogador com o número {numero} na tabela.\n'
                  'Tente novamente...')
        else:
            print('=-=' * 14)
            print(f'LEVANTAMENTO DO JOGADOR {time[numero]["nome"].upper()}:')
            for partida, gols in enumerate(time[numero]['gols']):
                if gols == 0:
                    print(f'\t=> Na {partida + 1}ª partida, não fez nenhum gol.')
                elif gols == 1:
                    print(f'\t=> Na {partida + 1}ª partida, apenas 1 gol.')
                else:
                    print(f'\t=> Na {partida + 1}ª partida, fez {gols} gols.')
            print(f'\nFoi um total de {time[numero]["total"]} gols!')
            print('=-=' * 14)
