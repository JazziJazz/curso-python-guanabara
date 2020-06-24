#  Programa que pensa em um número de zero a dez, e pergunta ao usuário em qual número ele está pensando. As tentativas
#  de acertar o número são computadas e depois exibidas na tela quando o usuário acertar.
from random import randint

number_tentatives = 1
random_number = randint(0, 10)
user_number = int(input('\033[6:36mBem-vindo ao Game da Adivinhação 2.0!\n'
                        '\033[1:33mEu pensei em um número, será que você consegue acertar em qual foi que eu pensei? '
                        'Lembrando, apenas números de zero até dez!\n\033[1:30mResposta: '))

while user_number != random_number:
    user_number = int(input('\033[31mErro! Você errou o número! Eu devo ser realmente muito bom, tente até acertar!'
                            '\n\033[1:30mResposta:'))
    number_tentatives += 1

print(52 * '\033[7:36m———')
print(f'\033[1:34mVOCÊ ACERTOU! Eu estava pensando mesmo no número {random_number}. Você gastou {number_tentatives} '
      f'para acertar que número eu estava pensando. Você é meio ruim nisso, né?')
print(52 * '\033[7:32m———')
