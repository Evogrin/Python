import random
a = str(input('First group name: '))
b = str(input('Second group name: '))
c = str(input('Third group name: '))
d = str(input('Fourth group name: '))
e = str(input('Last group name: '))
groups = [a,b,c,d,e]
random.shuffle(groups)
print(groups)
