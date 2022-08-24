prod = float(input('Preço do produto: '))
desc = (prod * 5)/100
print('Com desconto de 5%, o preço do produto passa a ser R${:.2f}'.format(prod - desc))
