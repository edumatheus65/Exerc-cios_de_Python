from random import shuffle, choice
nomes = input('Digite os nomes separados por espaço: ')
b = nomes.split( )
c = sorted(b)
print('A ordem da lista é: {}'.format(c))

