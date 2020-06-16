#  Programa que lê um número inteiro, verifica se ele é par ou impar e exibe o resultado na tela.

number = int(input('Digite um número, iremos verificar se ele é par ou impar: '))

if number % 2 == 0:
    print(f'O número {number} é PAR.')
else:
    print(f'O número {number} é IMPAR.')
