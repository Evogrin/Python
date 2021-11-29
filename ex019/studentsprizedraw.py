from random import choice
a = str(input('Type the name of first student: '))
b = str(input('Type the name of second student: '))
c = str(input('Type the name of third student: '))
d = str(input('Type the name of fourth student: '))
e = str(input('Type the name of last student: '))
list = (a,b,c,d,e)
print(choice(list))