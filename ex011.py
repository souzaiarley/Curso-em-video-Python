from math import ceil
from time import sleep
print('UTILIZE MEDIDAS EM METROS')
sleep(2)
larg = float(input('Informe a largura: '))
alt = float(input('Informe a altura: '))
a = larg * alt
lata = a/2
print('Para pintar {:.2f}m², use pelo menos {} latas de tinta.'.format(a, ceil(lata)))
