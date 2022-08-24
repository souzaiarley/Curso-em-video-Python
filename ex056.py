soma = maior = cont = 0
maisvelho = ''
for c in range(1, 5):
    print(f'-----{c}ª PESSOA-----')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('\033[31mPor favor, use "M" ou "F".\033[m\nSexo [M/F]: ')).strip().upper()
    soma = soma + idade
    if sexo == 'M':
        if idade > maior:
            maior = idade
            maisvelho = nome
    if sexo == 'F':
        if idade < 20:
            cont = cont + 1
print('A média de idade do grupo é {:.1f} anos;'.format(soma / 4))
print(f'O homem mais velho é {maisvelho} com {maior} anos;')
print(f'Ao todo, {cont} mulher(es) tem menos de 20 anos de idade.')
