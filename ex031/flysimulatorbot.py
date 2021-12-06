from time import sleep
print('-=-' * 25)
print('Welcome to Flybot!')
print('Flybot will calculate how much your plane ticket will cost!')
print('-=-' * 25)
name = input('Whats your name? ')
age = int(input(f'How old are you,{name}? '))
if age <= 17:
    print(f'Sorry {name} but Flybot only works for adults!')
    print('Please ask a adult to help you!')
else:
    distance = float(input('What is the flight distance? '))
    print('Processing...!')
    sleep(3)
    if distance <= 200:
        value1 = 0.5 * distance
        print(f'Ticket for your trip will cost R${value1:.2f}!')
    else:
        value2 = 0.45 * distance
        print(f'Ticket for your trip will cost R${value2:.2f}!')
    print('-=-' * 25)
    print('Thank you for using flybot!')
    print('-=-' * 25)
    exp = int(input('How was your experience using Flybot? (Type 1 for "bad", 2 for "resonable" and 3 for "great"): '))
    if exp == 3:
        print('Thanks for trusting us and using Flybot!')
    if exp == 2:
        input('What can we do to improve?\n ')
        print('Sending feedback to database...')
        sleep(3)
        print('Feedback noted, thanks for using Flybot!')
    if exp == 1:
        input('We are really sorry to hear it, what can we do to improve?\n ')
        print('Sending feedback to database...!')
        sleep(3)
        print('Feedback noted and sent to quality experts for improvement! Thanks for using Flybot!')