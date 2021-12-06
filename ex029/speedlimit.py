speed = int(input('Type car current speed: '))
if speed>60:
    print(f'You passed lane speed limit! Please slow down and drive carefully! you got a ticket of R${((speed-60)*7):.2f}')
else:
    print('You are under the speed limite, keep up driving carefully!')