from random import randint
from time import sleep
cont = 0
print('='*20)
print('JOGO DE PAR OU ÍMPAR')
print('='*20)
while True:
    sleep(2)
    player = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    while player != 'P' and player != 'I':
        print('\033[31mErro. Utilize [P/I]\033[m')
        player = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    jogada = int(input('Digite um valor (0 a 10): '))
    while jogada < 0 or jogada > 10:
        print('\033[31mErro. Escolha um valor de 0 a 10.\033[m')
        jogada = int(input('Digite um valor (0 a 10): '))
    pc = randint(0, 10)
    soma = jogada + pc
    print(f'Você jogou {jogada} e o PC jogou {pc}. Soma igual a {soma}')
    sleep(2)
    print('DEU', end=' ')
    if soma % 2 == 0:
        resultado = 'PAR.'
        print(resultado)
    if soma % 2 == 1:
        resultado = 'ÍMPAR.'
        print(resultado)
    sleep(2)
    if player == 'P':
        if resultado == 'PAR.':
            print('VOCÊ VENCEU!')
        else:
            print('VOCÊ PERDEU!')
            break
    if player == 'I':
        if resultado == 'ÍMPAR.':
            print('VOCÊ VENCEU!')
        else:
            print('VOCÊ PERDEU!')
            break
    cont = cont + 1
    sleep(2)
    print('Vamos jogar novamente...')
sleep(2)
print('=-' * 10)
print(f'GAME OVER!\nVocê venceu {cont} vez(es).')
