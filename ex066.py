cont = soma = n = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
print(f'Você digitou {cont} número(s) e a soma entre eles é {soma}.')
