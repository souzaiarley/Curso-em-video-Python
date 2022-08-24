peso = float(input('Seu peso (kg): '))
alt = float(input('Sua altura (cm): '))
imc = peso / ((alt/100) ** 2)
print('Seu IMC: {:.2f}'.format(imc))
print('Você está', end=' ')
if imc < 18.5:
    print('ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('no PESO IDEAL.')
elif 25 <= imc < 30:
    print('com SOBREPESO.')
elif 30 <= imc < 40:
    print('com OBESIDADE.')
elif 40 <= imc:
    print('com OBESIDADE MÓRBIDA.')
