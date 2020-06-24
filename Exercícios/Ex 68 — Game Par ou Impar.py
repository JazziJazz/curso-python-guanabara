#  Jogo do par ou impar. O jogador digita um número e escolhe par ou impar, o jogo só será interrompido se o jogador
#  perder. Após ele perder será exibido na tela o total de vitórias consecutivas.
from random import randint

maquina_par_ou_impar = None
contagem_vitorias = 0

while True:
    maquina_numero = randint(0, 10)
    number = int(input('\033[5:36mDigite um número de um a dez: '))

    while number < 0 or number > 10:
        number = int(input('\033[5:31mErro! Você digitou um número maior que dez, ou menor que zero. Não se joga assim!'
                           '\n\033[5:30mDigite um número de um a dez: '))

    pergunta = input('\033[1:35mVocê escolhe par ou impar? [P/I]\n\033[1:30mResposta: ').strip().upper()

    while pergunta not in 'P' and pergunta not in 'I':
        pergunta = input('\033[5:31mErro! Só há duas opções! Ou é par, ou é impar. Preste atenção, digite corretamente.'
                         '\n\033[1:30mResposta: ').strip().upper()

    if pergunta == 'P':
        maquina_par_ou_impar = 1
        if (number + maquina_numero) % 2 == 0:
            print('\033[5:32mVocê venceu! Parabéns.')
            contagem_vitorias += 1
        else:
            print(f'\033[5:31mVOCÊ PERDEU!\n\033[5:32mMas tudo bem, perder é normal. Você conseguiu ganhar '
                  f'{contagem_vitorias} vezes. ')
            break
    else:
        maquina_par_ou_impar = 2
        if (number + maquina_numero) % 2 != 0:
            print('\033[5:32mVocê venceu! Parabéns.')
            contagem_vitorias += 1
        else:
            print(f'\033[5:31mVOCÊ PERDEU!\n\033[5:32mMas tudo bem, perder é normal. Você conseguiu ganhar '
                  f'{contagem_vitorias} vezes. ')
            break
