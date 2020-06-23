#  Programa que lê o ano de nascimento de um grupo de pessoas e exibe na tela quantas delas são maiores de idade, e
#  quantas são menores de idade.
from datetime import datetime

ano = datetime.today().year
num_grupo = int(input('Digite o tamanho do grupo de pessoas:\nResposta: '))
maiores = 0
menores = 0

for i in range(1, num_grupo + 1):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))

    if (ano - ano_nascimento) >= 18:
        maiores += 1
    else:
        menores += 1

print(f'\033[32mAo total houve {maiores} pessoas maiores de idade neste grupo. E um total de {menores} menores de '
      f'idade.')
