print('{:=^25}'.format('CADASTRO'))
cont = conth = contf = 0
while True:
    idade = int(input('IDADE: '))
    if idade > 18:
        cont = cont + 1
    sexo = str(input('SEXO [M/F]:')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('\033[31mPor favor, utilize "M" ou "F".\033[m\nSEXO [M/F]: ')).strip().upper()
    if sexo == 'M':
        conth = conth + 1
    if sexo == 'F':
        if idade < 20:
            contf = contf + 1
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('\033[31mPor favor, utilize "S" ou "N".\033[m\nQuer continuar? [S/N]: ')).strip().upper()
    if escolha == 'N':
        break
print(f'Total de maiores de idade: {cont}')
print(f'Número de homens cadastrados: {conth}')
print(f'Número de mulheres com menos de 20 anos: {contf}')
