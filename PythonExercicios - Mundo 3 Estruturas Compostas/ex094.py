# Unindo dicionários e listas.
ficha = dict()
lista = []
media = 0
while True:
    ficha['Nome'] = str(input('Nome: '))
    ficha['Sexo'] = str(input('Sexo [M/F]: ').strip()[0])
    while ficha['Sexo'] not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F.')
        ficha['Sexo'] = str(input('Sexo [M/F]: '))
    ficha['Idade'] = int(input('Idade: '))
    media += ficha['Idade']
    lista.append(ficha.copy())

    ver = str(input('Quer continuar? [S/N]: '))
    while ver not in 'SsNn':
        print('Erro! Responda apenas S ou N')
        ver = str(input('Quer continuar? [S/N]: '))
    print('-' * 30)
    if ver in 'Nn':
        break

media = media / len(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for x in range(0, len(lista)):
    if lista[x]['Sexo'] in 'Ff':
        print(f'{lista[x]["Nome"]}, ', end='')
print(f'\nD) Lista das pessoas que estão acima da média de idade:')

for c in range(0, len(lista)):
    if (lista[c]['Idade']) > media:
        print(f'\tnome = {lista[c]["Nome"]}; sexo = {lista[c]["Sexo"].upper()}; idade = {lista[c]["Idade"]}')
