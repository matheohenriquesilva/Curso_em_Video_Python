# Exercitando módulos em Python (PROGRAMA PRINCIPAL).
from ex109 import moeda


def principal(num):
    print(f"A metade de {moeda.moedaf(num)} é {moeda.metade(num)}")
    print(f"O dobro de {moeda.moedaf(num)} é {moeda.dobro(num)}")
    print(f"Aumentando 10%, temos {moeda.aumento10(num)}")
    print(f"Diminuindo 25%, temos {moeda.diminuir(num)}")


aux = float(input("Digite o preço: R$"))
principal(aux)
