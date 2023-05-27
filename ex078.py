cont = n = maior = menor = 0
lista = []

while cont < 5:
    n = int(input(f'Digite um valor para a Posição {cont}: '))
    if (cont == 1):
        maior = menor = n
    else:
        if (n < menor):
            menor = n
        if (n > maior):
            maior = n
    lista.append(n)
    cont += 1

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end = '')
for c in range (0, 5):
    if (lista[c] == maior):
        print(f'{c}... ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end = '')
for c in range (0, 5):
    if (lista[c] == menor):
        print(f'{c}... ', end='')
print('\n')