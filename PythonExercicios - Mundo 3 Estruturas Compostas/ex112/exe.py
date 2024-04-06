# Exercitando módulos em Python (PROGRAMA PRINCIPAL).
from ex112.ultilidadesCeV import dados
from ex112.ultilidadesCeV import moeda


valor = dados.leiadinheiro("Digite o preço: R$")
moeda.resumo(valor, 20, 12)
