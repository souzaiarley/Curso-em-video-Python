vel = int(input('Informe a velocidade do carro(Km/h): '))
multa = (vel - 80) * 7
if vel > 80:
    print('Multado em R${:.2f}'.format(multa))
else:
    print('Dentro do limite de velocidade.')
