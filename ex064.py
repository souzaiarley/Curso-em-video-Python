cont = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont = cont + 1
    soma = soma + n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} número(s) e a soma entre eles é {soma}.')
