# Classificando Atletas.
from datetime import date
ano = int(input("Ano de nascimento: "))
idade = date.today().year - ano
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    clas = "MIRIM"
elif idade <= 14:
    clas = "INFANTIL"
elif idade <= 19:
    clas = "JUNIOR"
elif idade <= 25:
    clas = "SÊNIOR"
else:
    clas = "MASTER"
print("Classificação:", clas)
