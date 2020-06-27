#  Programa que lê cinco números e os coloca em uma lista, após fazer isso exibe qual foi o menor e o maior valores e
#  também exibe as suas posições.

lista = []
contagem = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto')

maior = None
menor = None
position_maior = None
position_menor = None

for i in range(0, 5):
    lista.append(int(input(f'\033[5:35mDigite o \033[5:32m{contagem[i].lower()} \033[5:35mnúmero, iremos adiciona-lo '
                           f'em uma lista: ')))

    if i == 4:
        for position, number in enumerate(lista):

            if maior is None or number > maior:
                maior = number
                position_maior = position
            if menor is None or number < menor:
                menor = number
                position_menor = position

        print(f'\033[5:35mO maior número é o: \033[5:32m{maior}\033[5:35m. Ele está na posição: '
              f'\033[5:32m{position_maior}\033[5:35m.\nO menor número é o: \033[5:32m{menor}\033[5:35m. Ele está na '
              f'posição: \033[5:32m{position_menor}\033[5:35m.')
