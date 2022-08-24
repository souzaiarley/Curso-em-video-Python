multi = 1
n = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {n}!')
for c in range(n, 0, -1):
    print(c, end=' ')
    if c > 1:
        print('x', end=' ')
    multi = multi * c
print(f'= {multi}')
