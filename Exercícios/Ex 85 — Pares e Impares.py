#  Programa que lê até dez valores e os armazena em uma lista, depois há mais duas listas com pares e impares, se o
#  valor for par, ele é armazenado na lista par, se for impar é armazenado na lista impar.

lista = [[], []]
numeros = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto', 'Sexto', 'Sétimo', 'Oitavo', 'Nono', 'Décimo')

for i in range(0, 10):
    numbers = int(input(f'\033[5:36mDigite o \033[5:33m{numeros[i].lower()}\033[5:36m valor, iremos armazena-lo em '
                        f'uma lista: '))

    if (numbers % 2) == 0:
        lista[0].append(numbers)
    else:
        lista[1].append(numbers)

print(f'\033[5:36mOs valores pares digitados foram: \033[5:33m{sorted(lista[0])}.\n'
      f'\033[5:36mOs valores impares digitados foram: \033[5:33m{sorted(lista[1])}.')
