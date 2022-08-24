from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = menor = 0
print('Os valores sorteados foram:', end=' ')
for c in range(0, 5):
    print(num[c], end=' ')
    if c == 0:
        maior = num[c]
        menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print(f'\nMAIOR valor sorteado: {maior}')
print(f'MENOR valor sorteado: {menor}')
