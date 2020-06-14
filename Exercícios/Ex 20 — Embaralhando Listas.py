# Programa que embaralha randomicamente todos os elementos de uma lista e entrega-os em uma nova ordem.
from random import shuffle

lista = []

for i in range(0, 5):
    lista.append(input('Digite um nome: '))

shuffle(lista)
print(lista)
