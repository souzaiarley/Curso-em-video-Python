print('{:=^40}'.format('10 TERMOS DE UMA P.A'))
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = pt + (10 - 1)*r
while pt <= dec:
    print(f'{pt} ', end='→ ')
    pt = pt + r
print('Fim.')
