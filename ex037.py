num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[1] converter para BINÁRIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL')
op = int(input('Sua opção: '))
while op != 1 and op != 2 and op != 3:
    print('Selecione apenas as opções de 1 a 3.')
    op = int(input('Sua opção: '))
if op == 1:
    print(f'{num} convertido para BINÁRIO é {bin(num)[2:]}.')
elif op == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}.')
elif op == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:]}.')
