#  Game pedra, papel ou tesoura. O jogador escolhe primeiro, e depois exibe o resultado na tela.
from random import randint
from pygame import mixer

try:
    mixer.init()
    mixer.music.load('musica/pygame/lover is a day.mp3')
    mixer.music.play()
except:
    print('Não foi possível iniciar o mixer do PyGame.')

escolha_maquina = randint(0, 3)
print(escolha_maquina)
escolha_player = int(input('Jogador! Que bom ver você por aqui! Pronto para jogar? Faça sua escolha!\n\n'
                           '1. Pedra.\n'
                           '2. Papel.\n'
                           '3. Tesoura.\n'
                           'Resposta: '))

while escolha_player < 1 or escolha_player > 3:
    print('Opção inválida jogador! Leia atentamente as opções e refaça sua jogada.\n\n'
          '1. Pedra.\n'
          '2. Papel.\n'
          '3. Tesoura.\n'
          'Resposta: ')

if escolha_player == 1 and escolha_maquina == 1:
    print('Empate! Um ponto para cada.')
elif escolha_player == 1 and escolha_maquina == 2:
    print('Háhá! Você é muito ruim, eu venci.')
elif escolha_player == 1 and escolha_maquina == 3:
    print('Wow. Você é muito bom, infelizmente eu perdi.')

if escolha_player == 2 and escolha_maquina == 1:
    print('Wow. Você é muito bom, infelizmente eu perdi.')
elif escolha_player == 2 and escolha_maquina == 2:
    print('Empate! Um ponto para cada.')
elif escolha_player == 2 and escolha_maquina == 3:
    print('Háhá! Você é muito ruim, eu venci.')

if escolha_player == 3 and escolha_maquina == 1:
    print('Háhá! Você é muito ruim, eu venci.')
elif escolha_player == 3 and escolha_player == 2:
    print('Wow. Você é muito bom, infelizmente eu perdi.')
elif escolha_player == 3 and escolha_maquina == 3:
    print('Empate! Um ponto para cada.')
