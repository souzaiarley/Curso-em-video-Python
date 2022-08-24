km = int(input('Distância da viagem em Km: '))
if km > 200:
    print('Preço da passagem será R${:.2f}'.format(km*0.45))
else:
    print('Preço da passagem será R${:.2f}'.format(km * 0.5))
