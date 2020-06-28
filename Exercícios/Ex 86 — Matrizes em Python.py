#  Programa que lê nove valores e os insere em uma matriz três por três.

matriz = [[], [], []]
numeros = ('Primeiro', 'Segundo', 'Terceiro')

for i in range(0, 3):
    for matrizes in range(0, 3):
        matriz[i].append(int(input(f'\033[5:36mDigite \033[5:33m{numeros[matrizes].lower()}\033[5:36m número da '
                                   f'\033[5:33m{numeros[i].lower()}\033[5:36m coluna: ')))
for i in range(0, 3):
    print()
    for n in range(0, 3):
        print(f'[ {matriz[i][n]} ]', end='')
