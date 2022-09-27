print("Bem vindo ao checkout da Aluguel Motors, por favor digite quantos dias e quantos kilometros rodados!")
dias = int(input('\nDias: '))*120
km = int(input('\nKm: '))*0.5
print('O total a ser pago é de R${},00! Obrigado por utilizar os serviços da Aluguel Motors :D'.format(dias+km))
