# (Progressão Aritmética v2.0).
print("Gerador de PA")
print('-=' * 10)
pa = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
contador = 1
while contador <= 10:
    print(f"{pa} ", end='➡ ')
    pa = pa + razao
    contador += 1
print("FIM", end='')
