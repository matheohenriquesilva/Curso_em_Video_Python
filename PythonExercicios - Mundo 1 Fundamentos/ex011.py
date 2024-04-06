# Pintando paredes.
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede, você precisará de {}l de tinta.'.format(lar, alt, area, tinta))
