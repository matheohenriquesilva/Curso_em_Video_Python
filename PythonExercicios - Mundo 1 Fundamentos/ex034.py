# Aumentos Multiplos.
salario = float(input("Qual é o salário do funcionário? R$"))
if salario <= 1250:
    novo = salario + (15 * salario / 100)
else:
    novo = salario + (10 * salario / 100)
print("Quem ganhava R${:.2f} pasa a ganhar R${:.2f} agora.".format(salario, novo))
