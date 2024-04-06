# (Tabuada v.2.0).
numero = int(input("Digite um número para ver sua tabuada: "))
multiplicador = 0
for i in range(1, 11):
    multiplicador += 1
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")

# Maneira mais simples.
'''for i in range(1, 11):
    print("{} x {:2} = {}".format(i, numero, numero * i))
'''