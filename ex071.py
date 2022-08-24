print('='*30)
print('{:^30}'.format("BANCO LUCY'S"))
print('='*30)
while True:
    n = int(input('Valor que deseja sacar: R$'))
    cont50 = n // 50
    if cont50 > 0:
        print(f'{cont50} cédula(s) de R$50')
    n = n - (cont50 * 50)
    if n == 0:
        break
    cont20 = n // 20
    if cont20 > 0:
        print(f'{cont20} cédula(s) de R$20')
    n = n - (cont20 * 20)
    if n == 0:
        break
    cont10 = n // 10
    if cont10 > 0:
        print(f'{cont10} cédula(s) de R$10')
    n = n - (cont10 * 10)
    if n == 0:
        break
    cont1 = n // 1
    if cont1 > 0:
        print(f'{cont1} cédula(s) de R$1')
    n = n - (cont1 * 1)
    if n == 0:
        break
print('='*30)
print('Obrigado, volte sempre!')
