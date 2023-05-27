abre = 0
fecha = 0
lista = str(input('Digite a expressão: '))
for c in range(0, len(lista)):
    if lista[c] == '(':
        abre += 1
    if lista[c] == ')':
        fecha += 1

if (abre == fecha):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')