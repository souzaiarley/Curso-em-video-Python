soma = cont = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            cont = cont + 1
            soma = soma + c
print(f'A soma dos {cont} valores solicitados é {soma}')
