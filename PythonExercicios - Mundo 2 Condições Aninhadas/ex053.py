# Detector de Palíndromo.
frase = str(input("Digite uma frase: ")).strip().upper()        # Tirei os espaços do começo e do fim, coloquei toda a frase em MAIÚSCULO.
palavras = frase.split()        # Separei a frase por palavras.
junto = ''.join(palavras)       # Juntei tudo sem espaços.
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}.")
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
