f = int(input('Temperatura em ºF: '))
c = (f - 32)/1.8
print('{} ºF = {:.0f} ºC'.format(f, c))
print('\033[30;43mFórmula\033[m  ({} °F - 32)/1.8 = {:.0f} °C'.format(f, c))
