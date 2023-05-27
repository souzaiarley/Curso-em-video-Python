lista = []
par = []
impar = []
n = 0
str = ""
while True:
    flag = 0
    n = int(input('Digite um valor: '))
    lista.append(n)
    str = input('Quer continuar? [S/N] ')
    if (str == 'n' or str == 'N'):
        break;

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'A lista copleta é {lista}')
for c in range (0, len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')