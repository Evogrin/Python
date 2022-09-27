salario_inicial = float(input('Digite o salário atual: R$'))
aumento = float(input('Digite a porcentagem salárial que deseja acrescentar! (apenas valor sem símbolos): '))
print('O salário com aumento ficará em: R$ {}'.format((salario_inicial*(aumento/100))+salario_inicial))
print('O valor do aumento foi de R$ {}'.format(salario_inicial*(aumento/100)))