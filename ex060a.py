multi = 1
n = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {n}!')
while n > 0:
    print(f'{n}', end=' ')
    if n > 1:
        print('x', end=' ')
    multi = multi * n
    n = n - 1
print(f'= {multi}')
