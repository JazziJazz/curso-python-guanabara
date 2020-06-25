#  Programa que exibe algumas informações sobre o Brasileirão de 2019. Exibe apenas os cinco primeiros colocados, os
#  últimos quatro colocados da tabela, depois exibe a lista dos times em ordem alfabética e por fim em que posição da
#  tabela se encontra a Chapecoense.

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avai')

print('\033[5:32mOs primeiros cinco colocados da tabela:')
for i in range(0, 6):
    if i < 5:
        print(f'\033[5:30m{times[i]}', end=', ')
    else:
        print(f'\033[5:30m{times[i]}', end='.')

print('\n\n\033[5:32mOs últimos quatro colocados da tabela:')
for i in range(len(times)-1, 15, -1):
    if i > 16:
        print(f'\033[5:30m{times[i]}', end=', ')
    else:
        print(f'\033[5:30m{times[i]}', end='.')

print(f'\n\n\033[5:32mLista dos times em ordem alfabética:\n'
      f'\033[5:30m{sorted(times)}')

while True:
    time_pergunta = input('\n\033[5:32mQual time você deseja procurar a posição?\n\033[5:30mResposta: ')
    continuar = input(f'\033[5:33mO time {time_pergunta} se encontra na {times.index(time_pergunta) + 1}ª posição da '
                      f'tabela do Brasileirão.\n\033[5:30mGostaria de procurar um outro time? [S/N]: ')

    while continuar not in 'S' and continuar not in 'N':
        continuar = input('\033[5:31mErro! Só é permitido sim ou não, releia a pergunta e tente novamente.\n\033[5:30m'
                          'Gostaria de procurar outro time? [S/N]: ')

    if continuar == 'N':
        print('Até outra hora então.')
        break
