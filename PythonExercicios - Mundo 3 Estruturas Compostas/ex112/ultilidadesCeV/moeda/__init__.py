# Exercitando módulos em Python (PARTE DAS FUNÇÕES).
def metade(num):
    aux = num / 2
    aux = moedaf(preco=aux)
    return aux


def dobro(num):
    aux = num * 2
    aux = moedaf(preco=aux)
    return aux


def aumento(num=0, taxa=0):
    aux = num + (num / 100 * taxa)
    aux = moedaf(preco=aux)
    return aux


def diminuir(num=0, taxa=0):
    aux = num - (num / 100 * taxa)
    aux = moedaf(preco=aux)
    return aux


def moedaf(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(p=0, taxaA=10, taxaR=5):
    print('-' * 30)
    print("RESUMO DO VALOR".center(30))
    print('-' * 30)
    print(f"Preço analisado: \t{moedaf(p)}")
    print(f"Dobro do preço: \t{dobro(p)}")
    print(f"Metade do preço: \t{metade(p)}")
    print(f"{taxaA}% de aumento: \t{aumento(p, taxa=taxaA)}")
    print(f"{taxaR}% de redução: \t{diminuir(p, taxa=taxaR)}")
    print('-' * 30)
