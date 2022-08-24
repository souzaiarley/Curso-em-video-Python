from random import randint
from time import sleep
print('\033[33m=-\033[m'*28)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m=-\033[m'*28)
sleep(1)
num = randint(0, 5)
resp = int(input('Em que número eu pensei? '))
while resp < 0 or resp > 5:
    resp = int(input('\033[31mErro! O número tem que ser entre 0 e 5!\033[m\nEm que número eu pensei? '))
if num == resp:
    print('\033[32mParabéns! Você venceu!')
else:
    print(f'\033[31mVOCÊ PERDEU! Eu pensei no número {num} e não no {resp}!')
