from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("\033[31mERRO ao ler o arquivo!\033[m")
    else:
        cabecalho("PESSOA CADASTRADAS")
        print(a.read())
