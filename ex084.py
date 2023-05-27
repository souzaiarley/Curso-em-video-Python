maior = menor = 0
lista = []

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    lista.append([nome, peso])
    if len(lista) == 1:
        menor = maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
    op = input('Quer continuar? [S/N] ')
    if (op == 'n' or op == 'N'):
        break;

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')

print(f'O maior peso foi de {maior}kg. Peso de', end = ' ')
for c in range(len(lista)):
    if lista[c][1] == maior:
        print(f'[{lista[c][0]}]', end=' ')

print(f'\nO menor peso foi de {menor}kg. Peso de', end = ' ')
for c in range(len(lista)):
    if lista[c][1] == menor:
        print(f'[{lista[c][0]}]', end=' ')

print('\n')