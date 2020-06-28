#  Programa que lê o nome e o peso de várias pessoas e depois exibe na tela uma lista com as pessoas mais pesadas, mais
#  leves e quantas pessoas foram cadastradas.

lista = []
dados = []

mais_pesadas = []
mais_leves = []

maior_peso = []
menor_peso = []
pessoas_cadastradas = 0

while True:
    dados.append(input('\033[5:32mDigite o nome da pessoa: '))
    dados.append(float(input('\033[5:32mQual é o peso dessa pessoa?: ')))
    lista.append(dados[:])
    pessoas_cadastradas += 1

    if dados[1] >= 100:
        mais_pesadas.append(dados[0])
    if dados[1] <= 70:
        mais_leves.append(dados[0])

    if pessoas_cadastradas == 1:
        maior_peso.append(dados[:])
        menor_peso.append(dados[:])
    else:
        if dados[1] > maior_peso[0][1]:
            maior_peso.clear()
            maior_peso.append(dados[:])
        if dados[1] < menor_peso[0][1]:
            menor_peso.clear()
            menor_peso.append(dados[:])

    dados.clear()

    pergunta = input('\033[5:33mVocê deseja cadastrar mais uma pessoa? \033[5:36m[S/N]: ').strip().upper()

    while pergunta not in 'S' and pergunta not in 'N':
        pergunta = input('\033[5:31mErro! Só há duas respostas possíveis, sim ou não. Qualquer reposta diferente é '
                         'desconsidera.\n\033[5:33mVocê deseja cadastrar mais uma pessoa? \033[5:36m[S/N]: ')

    if pergunta == 'N':
        print(f'\033[5:36mA lista com as pessoas mais PESADAS: \n\033[5:33m{mais_pesadas}\033[5:36m.\nA lista com as '
              f'pessoas mais LEVES: \n\033[5:33m{mais_leves}\033[5:36m.\nA pessoa mais PESADA é o(a): '
              f'\n\033[5:33m{maior_peso}\033[5:36m.\nA pessoa mais LEVE é o(a): \n\033[5:33m{menor_peso}\033[5:36m.\n'
              f'A lista completa é: \n\033[5:33m{lista}\nAo total você cadastrou: {pessoas_cadastradas} pessoas.')
        break
