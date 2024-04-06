# Verificando as primeiras letras de um texto.
cid = str(input("Em que cidade você nasceu? ")).strip()
print(cid[:5].upper() == 'SANTO')
# OU
# palavras = (cid.upper()).split()
#print(palavras[0] == 'SANTO')
# OU
# print('SANTO' in palavras[0])