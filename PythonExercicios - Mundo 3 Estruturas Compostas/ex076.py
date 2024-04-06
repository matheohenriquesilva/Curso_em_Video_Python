# Lista de Preços com Tupla.
produtos = (('Lápis', 1.50), ('Borracha', 1.25), ('Caderno', 25.00), ('Estojo', 28.00), ('Compasso', 8.99), ('Mochila', 140.35))
print('=' * 40)
print('{:^40}'.format("LISTAGEM DE PREÇOS"))
print('=' * 40)
for p in produtos:
    print("{:.<30}R$ {:>6,.2f}".format(p[0], p[1]))
print('-' * 40)
