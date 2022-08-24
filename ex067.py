from time import sleep
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    print('--'*10)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
print('--'*10)
print('Fim do programa.')
print('--'*10)
