from random import randint
from time import sleep
cont = 1
print('Vou pensar em um número entre 0 e 10... Tente adivinhar')
print('Hmm...')
sleep(3)
pc = randint(0, 10)
player = int(input('Em que número eu pensei? '))
while player < 0 or player > 10:
    print('O número tem que ser entre 0 e 10!')
    player = int(input('Em que número eu pensei? '))
while player != pc:
    if player < pc:
        print('Mais... Tente novamente.', end='')
    elif player > pc:
        print('Menos... Tente novamente', end='')
    player = int(input(' Em que número eu pensei? '))
    while player < 0 or player > 10:
        print('O número tem que ser entre 0 e 10!')
        player = int(input('Em que número eu pensei? '))
    cont = cont + 1
if cont == 1:
    print('Acertou de primeira!')
else:
    print(f'Acertou com {cont} tentativa(s). Parabéns!')
