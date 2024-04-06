# Sistema interativo de ajuda em Python.
from time import sleep
cores = {'sem': '\033[m',
         'vermelho': '\033[0;30;41m',
         'verde': '\033[0;30;42m',
         'amarelo': '\033[0;30;43m',
         'azul': '\033[0;30;44m',
         'roxo': '\033[0;30;45m',
         'branco': '\033[7;30m'
         }


def ajudar(comando):
    colorir(f'Acessando o manual do comando {comando}', 'azul')
    print(f"{cores['branco']}", end='')
    help(comando)
    print(f"{cores['sem']}", end='')
    sleep(1.5)


def colorir(mensagem, cor='sem'):
    tam = len(mensagem) + 4
    print(f"{cores[f'{cor}']}", end='')
    print('-' * tam)
    print(f'  {mensagem}')
    print('-' * tam)
    print(f"{cores['sem']}", end='')
    sleep(1)


while True:
    colorir('SISTEMA DE AJUDA PyHELP', 'verde')
    ajuda = str(input('Digite o nome de uma função ou biblioteca: ')).strip().lower()
    if ajuda == 'fim':
        break
    else:
        ajudar(ajuda)
colorir('Até logo!',  'vermelho')
