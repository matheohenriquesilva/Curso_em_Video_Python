# Gerenciador de Pagamentos.
print('{:=^40}'.format(" LOJAS GUANABARA "))
preco = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input("Qual sua opção? "))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcelas = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f} SEM JUROS".format(parcelas))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcelas = total / totparc
    print("Sua compra será parcealda em {}x de R${:.2f}".format(totparc, parcelas))
else:
    total = 0
    print("OPAÇÃO INVÁLIDA de pagamento. Tente novamente!")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, total))
