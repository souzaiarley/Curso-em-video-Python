from datetime import date
atual = date.today().year
nascimento = int(input('Ano que você nasceu: '))
idade = atual - nascimento
anos = 0
print(f'SUA IDADE EM {atual}: {idade} ANOS.')
if idade < 18:
    anos = 18 - idade
    print(f'Ainda faltam {anos} ano(s) para o alistamento.')
    print(f'Você deverá se alistar em {atual + anos}.')
elif idade == 18:
    print('CHEGOU A SUA VEZ. VOCÊ DEVE SE ALISTAR IMEDIATAMENTE.')
if idade > 18:
    anos = idade - 18
    print(f'Seu alistamento obrigatório foi há {anos} ano(s).')
    print(f'Seu alistamento obrigatório foi em {atual - anos}.')
