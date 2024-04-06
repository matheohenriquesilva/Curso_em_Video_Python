# Função que calcula área.
def controle():
    print("\tControle de Terrenos")
    print('-+' * 15)
    larg = float(input("LARURA (n): "))
    compr = float(input("COMPRIMENTO (n): "))
    area = larg * compr
    return print(f"A área de um terreno {larg}x{compr} é de {area}m².")


controle()
