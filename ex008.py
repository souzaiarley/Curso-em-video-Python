n = float(input('Medida em metros: '))
km = n/1000
hm = n/100
dam = n/10
dm = n*10
cm = n*100
mm = n*1000
print(f'{n} metros equivale: ')
print(f'{km}km\n{hm}hm\n{dam}dam')
print('{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(dm, cm, mm))
