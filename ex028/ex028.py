import random
print('Vou pensar em um número entre 0 a 6 tente advinhar!')
a = int(input('Em que número eu pensei?: '))
print('Processando...')
b = random.randint(0,6)
if a == b:
    print('Parabens! Você certou!')
else:
    print(f'Eu ganhei! Pensei no número {b}')
