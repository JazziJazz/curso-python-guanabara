#  Programa que gera cinco números em uma tupla e verifica nesta tupla qual é o maior e qual é o menor número, exibindo
#  esses mesmos números na tela.
from random import randint

random_numbers = (randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99))
maior = None
menor = None

for i in random_numbers:
    if maior is None or i > maior:
        maior = i
    if menor is None or i < menor:
        menor = i

print(f'\033[5:32mExibirei a lista dos números gerados aleatoriamente abaixo:\n\033[5:30m{random_numbers}\n'
      f'\033[5:36mO maior número é equivalente ao: \033[5:32m{maior}. '
      f'\033[5:36mO menor número é equivalente ao: \033[5:32m{menor}.')
