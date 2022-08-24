from random import  choice
alunos = (str(input('1º aluno: ')), str(input('2º aluno: ')), str(input('3º aluno: ')), str(input('4º aluno: ')))
print(f'O sorteado foi {choice(alunos)}.')
