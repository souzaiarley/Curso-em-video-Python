print('{:=^40}'.format('10 TERMOS DE UMA P.A'))
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = pt + (10 - 1)*r
for c in range(pt, dec + 1, r):
    print(c, end=' -> ')
print('ACABOU.')
