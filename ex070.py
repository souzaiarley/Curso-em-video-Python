print('{:=^30}'.format("LOJA LUCY'S"))
soma = cont = menor = cont1 = 0
barato = ''
while True:
    nome = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço do produto: R$'))
    soma = soma + preco
    cont1 = cont1 + 1
    if preco > 1000:
        cont = cont + 1
    if cont1 == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('\033[31mPor favor, utilize "S" ou "N".\033[m\nQuer continuar? [S/N]: ')).strip().upper()
    if escolha == 'N':
        break
print('{:=^20}'.format('FIM DO PROGRAMA.'))
print(f'Preço total: R${soma:.2f}')
print(f'Temos {cont} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {barato}, custando R${menor:.2f}')
