# Boletim com listas compostas.
lista = list()
alunos = list()
while True:
    nome = str(input("Qual o nome do Aluno(a)? "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    lista.append(media)
    alunos.append(lista[:])
    lista.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == 'N':
        break
print('-=' * 35)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print('=' * 30)
for n, d in enumerate(alunos):
    print(f"{n:<4}{d[0]:<10}{d[3]:>8.1f}")
while True:
    print('-=' * 35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(alunos) - 1:
        print(f"Notas de {alunos[opc][0]} são {alunos[opc][1]}")
print("<<< VOLTE SEMPRE >>>")
