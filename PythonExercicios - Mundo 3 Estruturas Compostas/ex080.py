# Lista ordenada sem repetições.
valores = list()
for cont in range(0, 5):
    numero = int(input("Digite um valor: "))
    if cont == 0 or numero > valores[-1]:
        valores.append(numero)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(valores):
            if numero <= valores[pos]:
                valores.insert(pos, numero)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1
print('-=' * 30)
print(f"Os valores digitados em ordem foram {valores}")
