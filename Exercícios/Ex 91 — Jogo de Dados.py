#  Programa que lê o nome de seis jogadores, e o resultado que cada um tirou rolando os dados, ao final, exibe o nome
#  do vencedor sabendo que este tirou a maior pontuação nos dados.
from random import randint

jogadores = []
jogadores_ordem = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto', 'Sexto')
vencedor_numero = vencedor_nome = None

for j in range(0, 3):
    nome_jogadores_dados = {'name': input(f'Qual o nome do {jogadores_ordem[j].lower()} jogador?: '),
                            'numero': randint(1, 6)}
    jogadores.append(nome_jogadores_dados.copy())

for i in range(0, len(jogadores)):
    if vencedor_numero is None or jogadores[i]['numero'] > vencedor_numero:
        vencedor_numero = jogadores[i]['numero']
        vencedor_nome = jogadores[i]['name']

print(f'O vencedor do game foi: {vencedor_nome}, ele tirou {vencedor_numero} nos dados.')
