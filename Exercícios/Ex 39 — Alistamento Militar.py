#  Programa que lê o ano de nascimento de uma pessoa e exibe na tela se é hora dela se alistar, se ela já se alistou
#  ou se já passou da hora de fazer o alistamento.
from datetime import datetime

ano_atual = datetime.today().year
alistamento = int(input('Você já se alistou no exército?\n\n'
                        '1. Sim, já me alistei.\n'
                        '2. Não, ainda não.\n\n'
                        'Resposta: '))

while alistamento < 1 or alistamento > 2:
    print('Resposta inválida, só há duas opções, releia até entender o contexto.\n'
          'Você já se alistou no exército?\n\n'
          '1. Sim, já me alistei.\n'
          '2. Não, ainda não.\n')

    alistamento = int(input('Resposta: '))

if alistamento == 1:
    print('Parabéns por cumprir os seus deveres como cidadão para com a pátria.')
else:
    idade = int(input('Qual seu ano de nascimento?\nResposta: '))

    if (ano_atual - idade) < 18:
        print(f'Você ainda é muito jovem para servir ao exército, você precisa ter completado ao menos dezoito anos. '
              f'Ainda falta {18 - (ano_atual - idade)} anos para você prestar contas com o seu país.')
    elif (ano_atual - idade) == 18:
        print(f'Corra já para a base burocrática do exército o mais rápido possível! É tempo de prestar contas com '
              f'o seu país e de servir a pátria mãe. Parabéns por completar dezoito anos.')
    else:
        print(f'Você está em débito com o seu país, isso é uma vergonha. Corra já para a fila de alistamento mais '
              f'próxima de sua residência, você deve {(ano_atual - idade) - 18} anos de serviço ao seu país.')
