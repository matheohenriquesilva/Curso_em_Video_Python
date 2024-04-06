# Função para Fatorial.
def fatorial(n, show=False):
    """
    -> CAlcula o Fatorial de um número:
    :param n: O número a ser fatorado.
    :param show: Mostrar ou não a conta.
    :return: O valor de um fatorial de um número.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
