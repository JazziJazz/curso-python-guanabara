# Programa que exibe o dobro de um número, o triplo e sua raiz quadrada.
from math import sqrt

number = int(input('Digite um número: '))
dobro = number * 2
triplo = number * 3
raiz = sqrt(number)

print(f'O dobro de {number} é {dobro}, o triplo é {triplo}.\n'
    f'A raiz quadrada é {raiz}.')
    