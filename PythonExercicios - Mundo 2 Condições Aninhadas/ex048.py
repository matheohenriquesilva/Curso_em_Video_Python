# Soma ímpares múltiplos de três.
soma = 0
contador = 0
for i in range(0, 501):
    if i % 2 != 0 and i % 3 == 0:
        contador += 1
        soma += i
print(f"A soma de todos os {contador} valores solicitados é {soma}")
