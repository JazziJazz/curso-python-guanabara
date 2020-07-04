from modulos import moeda

number = int(input('Digite um número, iremos fazer alguns cálculos: '))

print(f'O número {number} com desconto fica: {moeda.diminuindo(number)}.\nCom aumento ele fica: {moeda.aumento(number)}'
      f'.\nO dobro é igual a: {moeda.dobro(number)}.\nPor fim, a sua metade é igual a: {moeda.metade(number)}.')
