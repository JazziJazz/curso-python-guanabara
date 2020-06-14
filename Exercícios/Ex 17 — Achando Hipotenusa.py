# Programa que lê o cateto adjacente e o cateto oposto e encontra a hipotenusa de um triangulo retângulo.
from math import sqrt

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))

print(f'O valor da hipotenusa deste triangulo retângulo é de: {hipotenusa:.2f}.')
