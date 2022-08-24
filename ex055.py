peso = float(input(f'Peso da 1ª pessoa (kg): '))
maior = menor = peso
for c in range(2, 6):
    peso = float(input(f'Peso da {c}ª pessoa (Kg): '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
