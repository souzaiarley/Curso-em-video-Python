times = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
         'Fluminense', 'América', 'Atlético GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
         'Athletico Paranaense', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('=-' * 12)
print('BRASILEIRÃO 2021')
for c in range(1, 21):
    print(f'{c}º {times[c-1]}')
print('=-' * 12)
print('Os cinco PRIMEIROS colocados são:')
for c in range(1, 6):
    print(f'{c}º {times[c - 1]}')
print('=-' * 12)
print('Os quatro ÚLTIMOS colocados são:')
for c in range(17, 21):
    print(f'{c}º {times[c - 1]}')
print('=-' * 12)
print('Ordem ALFABÉTICA DOS TIMES:')
for c in range(1, 21):
    print(f'{c}º {sorted(times)[c-1]}')
print('=-' * 12)
print(f'O time da CHAPECOENSE se encontra na {times.index("Chapecoense") + 1}ª posição.')
