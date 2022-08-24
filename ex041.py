from datetime import date
atual = date.today().year
nasc = int(input('Data de nascimento: '))
idade = atual - nasc
clas = ''
print(f'Idade do atleta: {idade} anos.')
if idade <= 9:
    clas = 'MIRIM'
elif 9 < idade <= 14:
    clas = 'INFANTIL'
elif 14 < idade <= 19:
    clas = 'JÚNIOR'
elif 19 < idade <= 25:
    clas = 'SÊNIOR'
else:
    clas = 'MASTER'
print(f'Classificação: {clas}')
