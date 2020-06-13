# Programa que lê o salário de um funcionário e dá um aumento de acordo com as instruções do usuário do programa.

salario = float(input('Qual o salário do funcionário?: '))
aumento = int(input('Quantos porcento você deseja aumentar?: '))

calc = (salario + (aumento * salario / 100.0))
print(f'O salário original é de R${salario:.2f}.\nCom o aumento ele passa a ser R${calc:.2f}.')
