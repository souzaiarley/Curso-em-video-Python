lista = []
n = flag = 0
str = ""
while True:
    flag = 0
    n = int(input('Digite um valor: '))
    for c in lista:
        if (c == n):
            print('Valor duplicado! Não vou adicionar...')
            flag = 1
            break
    if (flag == 0):
        lista.append(n)
        print('Valor adicionado com sucesso...')
    str = input('Quer continuar? [S/N] ')
    if (str == 'n' or str == 'N'):
        break;

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Você digitou os valores {sorted(lista)}')