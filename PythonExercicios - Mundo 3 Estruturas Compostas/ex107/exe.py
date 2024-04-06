# Exercitando módulos em Python (PROGRAMA PRINCIPAL).
from ex107 import moeda


def principal(num):
    print(f"A metade de R${num:.1f} é R${moeda.metade(num):.1f}")
    print(f"O dobro de R${num:.1f} é R${moeda.dobro(num):.1f}")
    print(f"Aumentando 10%, temos R${moeda.aumento10(num):.1f}")


aux = float(input("Digite o preço: R$"))
principal(aux)
