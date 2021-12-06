from random import choice
from time import sleep
print('<-' * 28)
print('Thinking about a number btween 1-5, try and guess!')
print('->' * 28)
number = int(input('Type a number: '))
randnumber = [0, 1, 2, 3, 4, 5]
answer = choice(randnumber)
print('PROCESSING...')
sleep(2)

if(number != answer):
    print('I won! I thought about number {} not {}!'.format(answer, number))
else:
    print('Well done, you won!')