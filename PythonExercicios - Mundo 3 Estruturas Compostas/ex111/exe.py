# Exercitando módulos em Python (PROGRAMA PRINCIPAL).
from ex111.ultilidadesCeV import dados
from ex111.ultilidadesCeV import moeda


valor = float(input("Digite o preço: R$"))
moeda.resumo(valor, 20, 12)
