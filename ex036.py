casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos anos deseja pagar? '))
prest = casa / (anos*12)
cond = ''
if prest > (sal*30)/100:
    cond = 'NEGADO'
else:
    cond = 'APROVADO'
print('Para pagar a casa de valor R${:.2f} em {} anos, a prestação será de R${:.2f}\nEMPRÉSTIMO {}.'
      .format(casa, anos, prest, cond))
