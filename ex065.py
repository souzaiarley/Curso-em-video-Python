cont = soma = n = maior = menor = 0
op = ''
while op != 'N':
    n = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while op != 'S' and op != 'N':
        print('Por favor, use "S" ou "N".')
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
print('Você digitou {} número(s) e a média entre eles é {:.2f}'.format(cont, soma / cont))
print(f'O maior valor foi {maior} e o menor foi {menor}.')
