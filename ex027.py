nome = str(input('Nome completo: ')).strip().title()
pn = nome.split()[0]
un = nome.split()[len(nome.split()) - 1]
print(f'Seu primeiro nome é {pn}.')
print(f'Seu último nome é {un}.')
