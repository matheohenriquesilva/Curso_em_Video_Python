# Dicionário em Python.
aluno = dict()
aluno["nome"] = str(input("Nome: "))
aluno["média"] = float(input(f"Média de {aluno['nome']}: "))
if aluno["média"] >= 7:
    aluno["situacao"] = "Aprovado"
elif aluno["média"] < 5:
    aluno["situacao"] = "Reprovado"
else:
    aluno["situacao"] = "Recuperação"
print('-=' * 50)
for k, v in aluno.items():
    print(f"\t- {k} é igual a {v}")
