#  Programa que lê nove valores e os insere em uma matriz três por três. Ao término, mostra a soma de todos valores
#  pares, a soma dos valores da terceira coluna, o maior valor da segunda linha.

matriz = [[], [], []]
numeros = ('Primeiro', 'Segundo', 'Terceiro')
soma_pares = 0

for i in range(0, 3):
    for matrizes in range(0, 3):
        number = int(input(f'\033[5:36mDigite \033[5:33m{numeros[matrizes].lower()}\033[5:36m número da '
                           f'\033[5:33m{numeros[i].lower()}\033[5:36m coluna: '))
        matriz[i].append(number)

        if number % 2 == 0:
            soma_pares += number

for i in range(0, 3):
    print()
    for n in range(0, 3):
        print(f'[{matriz[i][n]:^5}]', end='')

print(f'\n\033[5:36mA soma total dos valores pares é de: \033[5:33m{soma_pares}\033[5:36m.\n'
      f'A soma dos valores da terceira coluna é: \033[5:33m{matriz[0][2] + matriz[1][2] + matriz[2][2]}\033[5:36m.\n'
      f'\033[5:36mO maior valor da segunda linha é: \033[5:33m{max(matriz[1])}\033[5:36m.')