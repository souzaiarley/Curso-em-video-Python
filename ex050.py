n = soma = cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print(f'Dos 6 valores digitados, {cont} são pares e a soma entre eles é {soma}.')
