# Alistamento Militar.
from datetime import date
nasc = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - nasc
print("Quem nasceu em {} tem {} em {}.".format(nasc, idade, atual))
if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    faltam = 18 - idade
    ano = atual + faltam
    print("Ainda faltam {} anos para o alistamento".format(faltam))
    print("Seu alistamento será em {}".format(ano))
else:
    passou = idade - 18
    ano = atual - passou
    print("Você já deveria ter se alistado há {} anos.".format(passou))
    print("Seu alistamento foi em {}".format(ano))
