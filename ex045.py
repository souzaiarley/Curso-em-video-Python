from random import randint
from time import sleep
lista = ['PEDRA', 'PAPEL', 'TESOURA']
print('{:=^40}'.format('PEDRA, PAPEL E TESOURA'))
pc = randint(1, 3)
print('[1] PEDRA\n[2] PAPEL\n[3] TESOURA')
player = int(input('Sua opção: '))
while player != 1 and player != 2 and player != 3:
    print('Opção inválida. Tente novamente.')
    player = int(input('Sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(0.6)
print('=-'*11)
print(f'Jogador jogou {lista[player - 1]}')
print(f'PC jogou {lista[pc - 1]}')
print('=-'*11)
if pc == player:
    print('\033[33mEMPATE\033[m')
elif player == 1 and pc == 3 or player == 2 and pc == 1 or player == 3 and pc == 2:
    print('\033[32mJOGADOR VENCE\033[m')
else:
    print('\033[31mPC VENCE\033[m')
