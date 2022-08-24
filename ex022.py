from time import sleep
nome = str(input('Digite o nome completo: ')).strip()
print('Analisando...'), sleep(3)
print(f'Seu nome em MAIÚSCULO é {nome.upper()}.')
print(f'Seu nome em MINÚSCULO é {nome.lower()}.')
nse = nome.replace(' ', '')
print(f'Seu nome possui {len(nse)} letras.')
print(f'Seu primeiro nome é {nome.split()[0].upper()} e possui {len(nome.split()[0])} letras.')
