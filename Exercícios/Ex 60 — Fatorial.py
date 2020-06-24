#  Programa que calcula um fatorial de um número. Utilizando o While ao invés do for.
from time import sleep

fatorial = int(input('\033[5:32mDigite um número referente a uma fatorial: '))
armazenamento = 1
print(f'\033[5:31m{fatorial}! = ', end='')

while fatorial != 0:
    armazenamento *= fatorial

    if fatorial > 1:
        print(f'\033[5:36m{fatorial}', end='x')
    else:
        print(f'\033[5:36m{fatorial} = ', end='')

    fatorial -= 1

sleep(3)
print(f'\033[5:31m{armazenamento}.\n\033[5:30mEste é o resultado de sua fatorial, até a próxima.')
