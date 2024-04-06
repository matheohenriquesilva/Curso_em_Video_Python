# Catetos e Hipotenusa.
from math import hypot
catO = float(input('Comprimento do cateto oposto: '))
catA = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(catO, catA)))

'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''