print('{:=^32}'.format("LOJA LUCY'S"))
valor = float(input('Valor das compras: R$'))
vd = 0
parcela = 0
print('FORMAS DE PAGAMENTO:\n[1] à vista no dinheiro \033[32m(Desconto de 10%)\033[m'
      '\n[2] à vista no cartão\033[32m (Desconto de 5%)\033[m\n[3] 2x no cartão (Sem juros)'
      '\n[4] 3x ou mais no cartão \033[31m(Juros de 20%)\033[m')
op = int(input('Sua opção: '))
while op != 1 and op != 2 and op != 3 and op != 4:
    print('Opção inválida. Tente novamente.')
    op = int(input('Sua opção: '))
if op == 1:
    vd = (valor * 10)/100
    print('VALOR A SER PAGO:\nR${:.2f} - 10% = \033[32mR${:.2f}\033[m'.format(valor, valor - vd))
if op == 2:
    vd = (valor * 5)/100
    print('VALOR A SER PAGO:\nR${:.2f} - 5% = \033[32mR${:.2f}\033[m'.format(valor, valor - vd))
if op == 3:
    print('VALOR DA PARCELA (mês):\n2x de \033[32mR${:.2f}\033[m'.format(valor / 2))
if op == 4:
    parcela = int(input('Em quantas parcelas? (mínimo de 3x): '))
    while parcela < 3:
        print('A quantidade mínima de parcelas é 3.')
        parcela = int(input('Em quantas parcelas? (mínimo de 3x): '))
    vd = (valor * 20) / 100
    print('VALOR DA PARCELA (mês):\n{}x de \033[32mR${:.2f}\033[m'.format(parcela, (valor + vd) / parcela))
