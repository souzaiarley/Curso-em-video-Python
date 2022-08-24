a = float(input('Primeiro lado do triângulo: '))
b = float(input('Segundo lado do triângulo: '))
c = float(input('Terceiro lado do triângulo: '))
if a < b + c and b < a + c and c < a + b:
    print('Com os 3 segmentos É POSSÍVEl formar um triângulo.')
else:
    print('Os 3 segmentos NÃO FORMAM um triângulo.')
