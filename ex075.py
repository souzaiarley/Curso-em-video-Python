num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print('Os valores digitados foram: ', end='')
cont = cont2 = cont3 = 0
for c in num:
    print(c, end=' ')
    if c == 9:
        cont += 1
    if c == 3:
        cont3 += 1
    if c % 2 == 0:
        cont2 += 1
print(f'\nO número "9" foi escolhido {cont} vez(es);')
if cont3 > 0:
    print(f'O valor "3" apareceu na {num.index(3)+1}ª posição;')
if cont3 == 0:
    print('Não houve ocorrência do número "3";')
if cont2 == 0:
    print('Não houve ocorrência de números pares.')
if cont2 > 0:
    print('Os valores pares digitados foram:', end=' ')
    for c in num:
        if c % 2 == 0:
            print(c, end=' ')
