# Número por Extenso.
contador = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if 0 <= numero <= 20:
        break
    print("Tente novamente.", end='')
print(f"O número digitado foi {contador[numero]}")
