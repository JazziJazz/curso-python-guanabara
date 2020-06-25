#  Programa que lê quatro números inteiros e os armazena em uma tupla, verifica quantas vezes o número nove apareceu e
#  em que posição está armazenada o número três, além de exibir quais foram os números pares dentro dessa tupla. Se não
#  houver nenhum nove, ou nenhum número três, não faça nada, apenas exiba que não possui números.

numeros = (int(input('Digite o primeiro número: ')), int(input('Digite o primeiro número: ')),
           int(input('Digite o primeiro número: ')), int(input('Digite o primeiro número: ')))
cont = 0
position = None
count_pares = 0

for i in numeros:
    if i == 9:
        cont += 1

    if i == 3:
        position = (numeros.index(3) + 1)

if position is not None:
    print(f'O número nove aparece um total de: {cont} vezes.\nO número três está na posição: {position}.\nOs números '
          f'pares digitados foram iguais a: ', end='')
else:
    print(f'O número nove aparece um total de: {cont} vezes.\nO número três não aparece nem uma única vez.\nOs números '
          f'pares digitados foram iguais a: ', end='')

for i in range(0, len(numeros)):
    if (numeros[i] % 2) == 0:
        count_pares += 1

for i in range(0, len(numeros)):
    if (numeros[i] % 2) == 0:
        if count_pares == 1:
            print(numeros[i], end='.')
        else:
            if i != 3:
                print(numeros[i], end=', ')
            else:
                print(numeros[i], end='.')
