from datetime import date
maior = menor = idade = ano = 0
for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da {c}ª pessoa:  '))
    idade = date.today().year - ano
    if idade >= 18:
        maior = maior + 1
    elif idade < 18:
        menor = menor + 1
print(f'Maiores de idade: {maior}')
print(f'Menores de idade: {menor}')
