prod = ('Lápis', 1.75, 'Borracha', 0.75, 'Lapiseira', 3, 'Caneta', 2, 'Apontador', 1,
        'Caderno', 12.5, 'Mochila', 85, 'Corretivo', 1.5)
print('='*32)
print('{:^32}'. format('PREÇOS'))
print('='*32)
for c in range(0, 16):
    if c % 2 == 0:
        print('{:.<25}'.format(prod[c]), end='')
    else:
        print('R$ {:.2f}'.format(prod[c]))
print('='*32)
