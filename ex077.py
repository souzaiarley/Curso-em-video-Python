words = ('CACHORRO', 'ESTOJO', 'GUITARRA', 'VIOLAO', 'TECLADO', 'CHUVA', 'MOUSE')
for c in words:
    print(f'\nNa palavra {c} temos: ', end='')
    for l in c:
        if l in 'AEIOU':
            print(l, end=' ')
