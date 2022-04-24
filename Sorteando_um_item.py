from random import choice
nomes = input('Me diga o nome dos alunos separado por espaços: ')
b = nomes.split( )
c = choice(b)
print('O aluno escolhido foi: {}'.format(c))

