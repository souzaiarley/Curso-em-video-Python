n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Média do aluno: {:.1f}'.format(media))
if media < 5:
    print('ALUNO REPROVADO')
elif media >= 7:
    print('ALUNO APROVADO')
else:
    print('ALUNO DE RECUPERAÇÃO')
