sexo = str(input('Seu sexo [M/F]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\033[31mPor favor, utilize "M" ou "F".\033[m\nSeu sexo [M/F]: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso.')
