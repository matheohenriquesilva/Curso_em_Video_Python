# Grupo da Maioridade.
from datetime import date
maiores = 0
menores = 0
for i in range(0, 7):
    pessoas = int(input(f"Em que ano a {i+1}ª pessoa nasceu? "))
    if date.today().year - pessoas >= 18:
        maiores += 1
    else:
        menores += 1
print(f"""\nAo todo tivemos {maiores} pessoas de idade
E também tivemos {menores} pessoas menores de idade""")
