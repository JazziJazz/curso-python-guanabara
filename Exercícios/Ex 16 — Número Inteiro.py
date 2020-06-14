# Programa que lê um número float e exibe o mesmo com apenas uma casa decimal.
from math import trunc

numero = float(input('Digite um número flutuante: '))
print(f'{trunc(numero)}')
