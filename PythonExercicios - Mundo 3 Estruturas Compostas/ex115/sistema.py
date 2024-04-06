from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print("Arquivo encontrado com sucesso!")
else:
    print("Arquivo não encontrado!")
    criarArquivo(arq)


while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print("\033[0;31mERRO: Digite uma opão válida!\033[m")
    sleep(1.5)
