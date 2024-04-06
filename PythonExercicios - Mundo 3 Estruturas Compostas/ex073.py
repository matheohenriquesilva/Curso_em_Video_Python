# Tuplas com Times de Futebol.
from time import sleep
barra = '-=' * 15
times = ('Grêmio', 'Santos', 'Atlético-MG', 'Avaí', 'Ceará',
         'CSA', 'Palmeiras', 'Fortaleza', 'São Paulo', 'Botafogo',
         'Flamengo', 'Cruzeiro', 'Fluminense', 'Goiás', 'Chapecoense',
         'Internacional', 'Bahia', 'Corinthians', 'Athlético-PR', 'Vasco')
print(barra)
print(f"Lista de times do Brasileirão: {times}")
print(barra)
sleep(1.5)
print(f"Os 5 primeiros são {times[0:5]}")
print(barra)
sleep(1.5)
print(f"Os 4 últimos são {times[16:20]}")
print(barra)
sleep(1.5)
print(f"Times em ordem alfabéticas: {sorted(times)}")
print(barra)
sleep(1.5)
print(f"O Corinthians está na {times.index('Corinthians')+1}ª posição")
