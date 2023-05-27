lista = []
n = 0
str = ""
while True:
    flag = 0
    n = int(input('Digite um valor: '))
    lista.append(n)
    str = input('Quer continuar? [S/N] ')
    if (str == 'n' or str == 'N'):
        break;

lista.sort()
lista.reverse()

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if (5 in lista):
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
