from random import choice
nomes = input('\nMe diga os nomes dos alunos separando-os por espaço: ').split( )
print(f'\nO aluno escolhido foi: {choice(nomes)}')