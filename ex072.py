ext = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE',
       'DEZ', 'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUINZE', 'DEZESSEIS', ' DEZESSETE',
       'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'{n} escrito por extenso é {ext[n]}.')
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        while op != 'S' and op != 'N':
            print('Utilize [S/N].')
            op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if op == 'N':
            break
    else:
        print('Tente novamente.')
print('Fim do programa!')
