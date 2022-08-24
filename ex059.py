from time import sleep
maior = 0

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('=-' * 10)
print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair')
op = int(input('>>> Sua opção: '))
while op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
    print('\033[31mOpção inválida.\033[m')
    sleep(1)
    print('=-' * 10)
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair')
    op = int(input('>>> Sua opção: '))
while op != 5:
    if op == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}.')
    elif op == 2:
        print(f'O produto de {n1} x {n2} é {n1 * n2}.')
    elif op == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        print(f'Entre {n1} e {n2}, o maior valor é {maior}.')
    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('Valores atualizados!')
    sleep(2)
    print('=-' * 10)
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair')
    op = int(input('>>> Sua opção: '))
    while op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
        print('\033[31mOpção inválida.\033[m')
        sleep(1)
        print('=-' * 10)
        print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair')
        op = int(input('>>> Sua opção: '))
print('ENCERRANDO', end='')
for c in range(1, 4):
    sleep(0.5)
    print('.', end='')
sleep(0.5)
print('\n=-=-=-=-=-=-=-=-')
print('Fim do programa!')
