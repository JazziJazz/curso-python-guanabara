#  Programa que exibe o valor do maior, menor número mas se os dois forem iguais, exibe na tela o resultado.

number = int(input('Digite o primeiro número: '))
number_two = int(input('Digite o segundo número: '))

if number > number_two:
    print(f'O número {number} é maior que o número {number_two}.')
elif number < number_two:
    print(f'O número {number_two} é maior que o número {number}.')
else:
    print('Não existe número maior ou menor, ambos são iguais.')