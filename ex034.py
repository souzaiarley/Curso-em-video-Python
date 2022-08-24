sal = float(input('Salário do funcionário: '))
va = 0
if sal > 1250:
    va = (sal*10)/100
else:
    va = (sal*15)/100
print('O novo salário passa a ser R${:.2f}'.format(sal + va))
