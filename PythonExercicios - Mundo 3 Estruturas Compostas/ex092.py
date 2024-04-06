# Cadastro de Trabalhador em Python.
from datetime import date
dataAno = date.today().year
rg = dict()
rg['nome'] = str(input("Nome: "))
rg['idade'] = int(input("Ano de Nascimento: "))
rg['idade'] = dataAno - rg['idade']
rg['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))
if rg['ctps'] != 0:
    rg['contratação'] = int(input("Ano de Contratação: "))
    rg['salario'] = float(input("Salário: R$"))
    rg['aposentadoria'] = rg['idade'] + ((rg['contratação'] + 35) - dataAno)
print('-=' * 30)
for k, v in rg.items():
    print(f"\t- {k} tem o valor {v}")
