# Analisando e gerando Dicionários.
def notas(*n, sit=False):
    x = dict()
    x['total'] = len(n)
    x['maior'] = max(n)
    x['menor'] = min(n)
    x['media'] = sum(n) / len(n)
    if sit:
        if x['media'] >= 7:
            x['situação'] = "BOA"
        elif x['media'] >= 5:
            x['situação'] = "RAZOÁVEL"
        else:
            x['situação'] = "RUIM"
    return x


resp = notas(5, 5, 8, 9, 10, 5)
print(resp)
print('=-' * 50)
resp = notas(2, 10, 7, 8, sit=True)
print(resp)
