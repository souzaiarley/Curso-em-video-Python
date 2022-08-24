print('{:=^40}'.format('10 TERMOS DE UMA P.A'))
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont1 = cont2 = 0
dec = pt + (10-1)*r
termos = 1
while pt <= dec:
    print(f'{pt} ', end='→ ')
    pt = pt + r
while termos != 0:
    print('PAUSA')
    termos = int(input('Quantos termos a mais deseja mostrar?: '))
    while termos < 0:
        termos = int(input('Erro. Digite um número válido.\nQuantos termos a mais deseja mostrar?: '))
    while cont1 < termos:
        print(f'{pt} ', end='→ ')
        cont1 = cont1 + 1
        cont2 = cont2 + 1
        pt = pt + r
    cont1 = 0
print('→ FIM')
print(f'Progressão finalizada. {cont2 + 10} termos foram mostrados.')
