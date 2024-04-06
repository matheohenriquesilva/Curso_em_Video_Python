# Radar Eletrônico.
velo = float(input("Qual é a velocidade atual do carro? "))
if velo > 80:
    multa = (velo - 80) * 7
    print("""MULTADO! Você excedeu o limete permitido que éde 80Km/h
Você deve pagar uma multa de R${}!""".format(multa))
print("Tenha um bom dia! Dirija com segurança!")
