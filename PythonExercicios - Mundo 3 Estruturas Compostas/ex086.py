# Matriz em Python.
matriz = [[], [], []]
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        if len(matriz[0]) < 3:
            matriz[0].append(valor)
        else:
            if len(matriz[1]) < 3:
                matriz[1].append(valor)
            else:
                if len(matriz[2]) < 3:
                    matriz[2].append(valor)
print('-=' * 50)
print("[ {:^6} ] [ {:^6} ] [ {:^6} ]".format(matriz[0][0], matriz[0][1], matriz[0][2]))
print("[ {:^6} ] [ {:^6} ] [ {:^6} ]".format(matriz[1][0], matriz[1][1], matriz[1][2]))
print("[ {:^6} ] [ {:^6} ] [ {:^6} ]".format(matriz[2][0], matriz[2][1], matriz[2][2]))
