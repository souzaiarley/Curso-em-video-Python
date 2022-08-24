cont = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[32m{c}\033[m', end=' ')
        cont = cont + 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {n} foi divisível {cont} vez(es).')
if cont == 2:
    print(f'{n} é um número PRIMO.')
else:
    print(f'{n} NÃO é um número PRIMO.')
