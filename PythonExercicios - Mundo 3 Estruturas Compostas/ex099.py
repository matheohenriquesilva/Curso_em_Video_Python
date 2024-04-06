# Função que descobre o maior.
from time import sleep
def maior(* num):
    cont = maior = 0
    print('-=' * 25)
    print("Analisando os valores passados...")
    sleep(0.8)
    for n in num:
        sleep(0.5)
        print(f"{n} ", end='')
        cont += 1
        if n > maior:
            maior = n
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
