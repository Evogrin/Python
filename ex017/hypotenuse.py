import math
Opposite = float(input('Type base lenght: '))
Adjacent = float(input('Type perpendicular lenght: '))
Hypotenuse = math.sqrt((Opposite*Opposite)+(Adjacent*Adjacent))
print(f'Hypotenuse lenght is: {Hypotenuse}')