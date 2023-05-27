lista = []
n = flag = 0

for c in range (0,5):
    flag = 0
    n = int(input("Digite um valor: "))

    for x in lista:
        if x == n:
            flag = 1
            break

    if flag == 1:
        print('Valor duplicado! Não vou adicionar...')
    else:
        for p in range (0, len(lista)+1):
            if p == len(lista):
                lista.append(n)
                print('Adicionado ao final da lista...')
                break;
            else:
                if n < lista[p]:
                    lista.insert(p, n)
                    print(f'Adicionado na posição {p} da lista...')
                    break;
                
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'Os valores digitados em ordem foram {lista}')    