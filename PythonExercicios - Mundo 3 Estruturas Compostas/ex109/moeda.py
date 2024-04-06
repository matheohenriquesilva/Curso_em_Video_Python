# Exercitando módulos em Python (PARTE DAS FUNÇÕES).
def metade(num):
    aux = num / 2
    aux = moedaf(preco=aux)
    return aux


def dobro(num):
    aux = num * 2
    aux = moedaf(preco=aux)
    return aux


def aumento10(num):
    aux = num + (num / 100 * 10)
    aux = moedaf(preco=aux)
    return aux


def diminuir(num):
    aux = num - (num / 100 * 25)
    aux = moedaf(preco=aux)
    return aux


def moedaf(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

