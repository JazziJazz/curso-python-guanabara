cadastro_jogador = {'nome': input('Qual é o nome do jogador(a)?: '), 'partida': int(input('Quantas partidas jogou?: '))}

for gols in range(0, cadastro_jogador['partida']):
    if gols == 0:
        cadastro_jogador['gols'] = [int(input(f'Quantos gols o jogador {cadastro_jogador["nome"]} marcou na {gols + 1} '
                                              f'partida?: '))]
    else:
        cadastro_jogador['gols'].append(int(input(f'Quantos gols o jogador {cadastro_jogador["nome"]} marcou na '
                                                  f'{gols + 1} partida?: ')))

for i in range(0, len(cadastro_jogador['gols'])):
    if i == 0:
        cadastro_jogador['total_gols'] = 0
        cadastro_jogador['total_gols'] += cadastro_jogador['gols'][i]
    else:
        cadastro_jogador['total_gols'] += cadastro_jogador['gols'][i]

for k, v in cadastro_jogador.items():
    print(f'O campo {k} possui o valor: {v}.')

print(f'\nO jogador {cadastro_jogador["nome"]} jogou um total de {cadastro_jogador["partida"]}.\n')

for i in range(1, cadastro_jogador["partida"] + 1):
    print(f'     → Na partida {i} ele fez: {cadastro_jogador["gols"][i - 1]} gols.')
print(f'Foi um total de: {cadastro_jogador["total_gols"]}.')
