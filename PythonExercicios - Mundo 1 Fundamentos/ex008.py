# Conversor de Medidas.
m = float(input('Uma distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{}Km\n{}Hm\n{}Dam\n{}Dm\n{}Cm\n{}mm'.format(km, hm, dam, dm, cm, mm))
