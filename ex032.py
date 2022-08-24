from datetime import date
ano = int(input('Informe o ano (Digite "0" para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é ano BISSEXTO!')
else:
    print(f'{ano} NÃO é ano BISSEXTO!')
