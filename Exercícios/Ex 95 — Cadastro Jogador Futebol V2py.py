jogadores = []
dados = {}
cod = 0

while True:
    dados['cód'] = cod
    dados['nome'] = input('Qual é o nome do jogador?: ').strip().title()
    dados['numero_partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou?: '))
    dados['gols'] = []
    dados['total_gols'] = 0

    for i in range(0, dados['numero_partidas']):
        dados['gols'].append(int(input(f'Quantos gols o jogador {dados["nome"]} marcou na {i + 1} partida?: ')))
        dados['total_gols'] += dados['gols'][i]

    cod += 1
    jogadores.append(dados.copy())
    dados.clear()

    pergunta = input('Deseja continuar? [S/N]: ').strip().upper()

    while pergunta not in 'S' and pergunta not in 'N':
        pergunta = input('\033[5:31mErro! Só há duas respostas possíveis, sim ou não.\n'
                         '\033[5:30mDeseja continuar? [S/N]: ').strip().upper()

    if pergunta == 'N':
        print(f'\n{50 * "="}\n{"Cód":<10}{"Nome":<20}{"Gols":^10}{"Total":>10}\n{50 * "="}')

        for i in range(0, len(jogadores)):
            print(f'[{jogadores[i]["cód"]:^5}]   {jogadores[i]["nome"]:.<21}  {jogadores[i]["gols"]}  '
                  f'{jogadores[i]["total_gols"]:>7}')

        while True:
            question = int(input('Deseja mostrar os dados de qual jogador?: '))

            while question > len(jogadores) and question != 999:
                question = int(input('Código inválido. Deseja mostrar os dados de qual jogador?: '))

            if question == 999:
                print('Programa encerrado.')
                break
            else:
                print(f'\nO jogador {jogadores[question]["nome"]} marcou um total de {jogadores[question]["total_gols"]} '
                      f'gols em {jogadores[question]["numero_partidas"]} partidas.\n')

                for i in range(0, len(jogadores[question]['gols'])):
                    print(f'O jogador {jogadores[question]["nome"]} marcou na sua {i + 1}º partida um total de '
                          f'{jogadores[question]["gols"][i]} gols.')
        break
