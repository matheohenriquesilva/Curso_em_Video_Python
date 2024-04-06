# Cadastro de Jogador de Futebol.
dados = dict()
dados['nome'] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas o {dados['nome']} jogou? "))
dados['gols'] = list()
for p in range(1, partidas + 1):
    dados['gols'].append(int(input(f"\tQuantos gols na partida {p}? ")))
gols = 0
for g in dados['gols']:
    gols += g
dados['total'] = gols
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f"O jogador {dados['nome']} jogou {partidas} partidas.")
for p, g in enumerate(dados['gols']):
    print(f'\t=> Na partida {p+1}, fez {g} gols.')
print(f"Foi um total de {dados['total']} gols.")
