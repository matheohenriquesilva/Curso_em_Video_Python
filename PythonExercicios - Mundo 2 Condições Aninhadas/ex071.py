# Simulador de Caixa Eletrônico.
barra = '=' * 15
print("{}\n{:-^30}\n{}".format(barra+barra, " BANCO THEo ", barra+barra))
valor = int(input("Que valor você quer sacar? R$"))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print(f"{barra+barra}\nVolte sempre ao BANCO THEo! Tenha um bom dia!")
'''
notas50 = valor // 50
notas10 = (valor % 50) // 10
notas1 = ((valor % 50) % 10) // 1
print(f"""Total de {notas50} cédulas de R$50
Total de {notas10} cédulas de R$10
Total de {notas1} cédulas de R$1""")
'''
