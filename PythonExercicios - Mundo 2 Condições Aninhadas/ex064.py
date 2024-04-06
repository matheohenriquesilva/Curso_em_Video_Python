# (Tratando vários valores v1.0).
num = soma = contador = 0
while num != 999:
    num = int(input("Digite um número [999 para parar]: "))
    if num != 999:
        soma += num
        contador += 1
print(f"Você digitou {contador} números e a soma entre eles foi {soma}.")
