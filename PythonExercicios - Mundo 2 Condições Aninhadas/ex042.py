# (Analisando Triângulos v2.0)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro seqmento: "))
if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR UM triângulo! ", end='')
    if r1 == r2 and r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print("ESCALENO")
    else:
        print("IsÓSCELES")
else:
    print("Os segmentos acuna NÃO PODEM FORMAR triângulo")
