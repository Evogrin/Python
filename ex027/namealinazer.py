name = str(input("Type you're full name: ")).strip().title().split()
print('Glad to meet you!\nYour firstname is {};\nyour last name is {}'.format(name[0], name[-1]))