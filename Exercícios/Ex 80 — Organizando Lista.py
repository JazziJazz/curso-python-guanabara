#  Programa que lê cinco números em uma lista, em seguida exibe essa mesma lista de forma ordenada, com os números
#  crescentes.
from random import randint

"""lista = [randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99),
         randint(0, 99), randint(0, 99), randint(0, 99)]
lista_two = lista[:]

for i in range(0, len(lista)):
    for numeros in range(0, len(lista)):
        if lista[i] < lista[numeros]:
            menor = lista[numeros]

            lista[numeros] = lista[i]
            lista[i] = menor

print(f'A primeira lista com minha ordenação própria: {lista}.\nA segunda lista, original: {lista_two}.\nA terceira '
      f'lista com ordenação: {sorted(lista_two)}.')"""

"""lista = [0, 0, 0, 0, 0]
contagem = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto', 'Primeira', 'Segunda', 'Terceira', 'Quarta',
            'Quinta')

for verification in range(0, len(lista)):
    if verification == 0:
        lista[len(lista) - 1] = int(input(f'\033[5:35mDigite o \033[5:32m{contagem[verification].lower()} \033[5:35mnú'
                                          f'mero, iremos adiciona-lo em uma lista: '))
        print(f'\033[5:35mAdicionei o \033[5:32m{contagem[verification].lower()} \033[5:35mnúmero ao \033[5:32mfinal '
              f'\033[5:35mda lista.\n')
    else:
        lista[verification] = int(input(f'\033[5:35mDigite o \033[5:32m{contagem[verification].lower()} \033[5:35mnúme'
                                        f'ro, iremos adiciona-lo em uma lista: '))
        print(f'O número {lista[verification]} foi adicionado na \033[5:32m{contagem[verification + 5].lower()}'
              f'\033[5:35m posição.\n')

    for numeros in range(0, len(lista)):
        if lista[verification] < lista[numeros]:
            lista[verification], lista[numeros] = lista[numeros], lista[verification]

print(lista)"""
