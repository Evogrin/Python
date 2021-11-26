salary = int(input('Type base salary: R$'))
payrise = int(input('Type the payrise in %(only number):'))
newsalary = salary+(salary*(payrise/100))
print(f'New salary is: R${newsalary}')