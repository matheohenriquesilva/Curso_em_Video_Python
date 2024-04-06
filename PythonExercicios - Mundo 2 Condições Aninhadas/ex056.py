# Analisador completo.
somaIdade = 0
maiorIdadeHomen = 0
nomeVelho = ''
totalMulheres20 = 0

for pessoas in range(1, 5):
    print(f"----- {pessoas}ª PESSOA -----")
    nome = str(input("NOME: ")).strip()
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO : [M/F]: ")).strip()
    somaIdade += idade
    if pessoas == 1 and sexo in 'Mm':
        maiorIdadeHomen = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomen:
        maiorIdadeHomen = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulheres20 += 1

mediaIdade = somaIdade / pessoas
print(f"A média de idade do grupo é de {mediaIdade} anos.")
print(f"O homem mais velho tem {maiorIdadeHomen} e se chama {nomeVelho}.")
print(f"Ao todo são {totalMulheres20} mulheres com menos de 20 anos.")
