#  Programa que lê um número e exibe na tela se este número é primo ou não.

number = int(input('Digite um número, iremos fazer alguns calculos e te dizer se ele é primo ou não.\nNúmero: '))
divisores = 0
primo = False

for i in range(1, number+1):
    if (number % i) == 0:
        divisores += 1
        print(f'\033[1:34m{i}', end=' ')
    else:
        print(f'\033[1:30m{i}', end=' ')

    if divisores == 2:
        primo = True

if primo is True:
    print(f'\n\n\033[1:32mO número {number} é primo, pois possui dois divisores.')
else:
    print(f'\n\n\033[1:31mO número {number} não é um número primo, pois possui mais que dois divisores.')
