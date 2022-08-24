from random import  shuffle
alunos = [str(input('1º aluno: ')), str(input('2º aluno: ')), str(input('3º aluno: ')), str(input('4º aluno: '))]
shuffle(alunos)
print('A ordem de apresentação será: ')
print(alunos)
