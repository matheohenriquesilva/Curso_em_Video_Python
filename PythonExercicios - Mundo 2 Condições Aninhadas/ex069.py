# Análise de dados do grupo.
tot18 = totH = totM20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input("Quer continuar? {S/N] ")).strip().upper()[0]
    if resposta == 'N':
        break
print(f"Total de pessoas com mais de 18 anos: {tot18}")
print(f"Ao todo temos {totH} homens cadastrados")
print(f"E temos {totM20} mulheres com menos de 20 anos")
