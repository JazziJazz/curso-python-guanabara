def jogador(x, y):
    if (x is None) or (x == ''):
        x = '<desconhecido>'

    return print(f'O jogador {x} marcou {y} gols nessa temporada.')


a = input('Digite o nome do jogador: ')
b = input('Quantos gols o jogador marcou?: ')

if b.isnumeric():
    int(b)
else:
    b = 0

jogador(a, b)
