# Aprovando Empréstimo.
valor = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))
parcelas = valor / (anos * 12)
print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(valor, anos, parcelas))
if parcelas <= (salario * 30 / 100):
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")
