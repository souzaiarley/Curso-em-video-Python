n = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
ninverso = n[::-1]
print(f'O inverso de {n} é {ninverso}')
if n == ninverso:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase NÃO é PALÍNDROMO!')
