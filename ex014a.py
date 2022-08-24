c = int(input('Temperatura em ºC: '))
f = (c * 1.8) + 32
print('{} ºC = {:.0f} ºF'.format(c, f))
print('\033[30;43mFórmula\033[m  ({} °C × 1.8) + 32 = {:.0f} °F'.format(c, f))
