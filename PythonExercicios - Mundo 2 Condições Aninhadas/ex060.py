# Cálculo do Fatorial.
numero = int(input("Digite um número para\ncalcular seu Fatorial: "))
contador = numero
fat = 1
print(f"Calculando {numero}! = ", end='')
while contador > 0:
    print(f"{contador}", end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fat *= contador
    contador -= 1
print(f"{fat}")
