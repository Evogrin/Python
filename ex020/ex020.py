from random import shuffle
lista = str(input('\nDigite o nome dos alunos que devem apresentar o trabalho separando-os por espaço!: ')).split( )
shuffle(lista)
print(f'A ordem de aprensentação é:\n {lista}')
