print('{:=^40}'.format('SEQUÊNCIA DE FIBONACCI'))
ant = pro = 0
cont = 2
atu = 1
termos = int(input('Quantos termos deseja mostrar?: '))
print('0 → 1 →', end=' ')
while cont < termos:
    pro = atu + ant
    print(pro, end=' → ')
    ant = atu
    atu = pro
    cont = cont + 1
print('Fim.')
