# Funções para votação.
def func_vontacao(ano):
    from datetime import date
    idade = date.today().year - ano
    print('-' * 20)
    print(f"Com {idade}: ", end='')
    if idade <= 16:
        return print("NÃO VOTA.")
    elif idade < 18 or idade > 70:
        return print("VOTO OPCIONAL.")
    else:
        return print("VOTO OBRIGATÓRIO.")


func_vontacao(int(input("Em que ano você nasceu? ")))
