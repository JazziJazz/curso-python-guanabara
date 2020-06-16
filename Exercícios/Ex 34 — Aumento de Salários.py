#  Programa que lê o valor do salário de um funcionário, se ele ganhar mais que mil duzentos e cinquenta, deverá
#  ganhar um aumento de dez porcento, se for inferior a isso, deverá ganhar um aumento de quinze porcento.

salario = float(input('Qual é o valor do salário?\nRESPOSTA: '))

if salario > 1250:
    calculo = (salario + (10 * salario / 100.0))
else:
    calculo = (salario + (15 * salario / 100.0))

print(f'O valor do salário a ser calculado é igual a R${calculo:.2f}.')
