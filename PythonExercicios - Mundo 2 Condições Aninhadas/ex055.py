# Maior e menor da sequência.
maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input(f"Peso da {pessoas}ª pessoa: "))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"""\nO maior peso lido foi de {maior}Kg
O menor peso lido foi de {menor}Kg""")
