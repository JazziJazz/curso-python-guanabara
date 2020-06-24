#  Programa que lê dois números e exibe na tela diversas opções sobre o que fazer com esses números, no quesito
#  matemática.
from time import sleep

one = float(input('\033[5:30mDigite o primeiro número: '))
two = float(input('\033[5:30mDigite o segundo número: '))
options = None

while options is None or (options > 5) or (options < 1):
    options = int(input(f'\n\033[5:32mOs números digitados por você foram: {one}, {two}. O que quer fazer com eles? '
                        f'selecione o número da opção referente a sua escolha. \n\n'
                        f'1. Somar.\n'
                        f'2. Multiplicar.\n'
                        f'3. Maior e menor.\n'
                        f'4. Digitar novos números.\n'
                        f'5. Encerrar o programa.\n\n'
                        f'\033[5:30mResposta: '))

    if options == 1:
        print(f'Você escolheu a opção de soma.\nA soma entre {one} e {two} é igual a: {one + two}.')
        sleep(4.5)
        options = None
    elif options == 2:
        print(f'Você escolheu a opção de multiplicação.\nA multiplicação entre {one} e {two} é igual a: {one * two}.')
        sleep(4.5)
        options = None
    elif options == 3:
        if one > two:
            print(f'Você escolheu a opção maior e menor. O maior número é o {one}, ele está a {one - two} casas '
                  f'decimais de distância.')
            sleep(4.5)
            options = None
        elif two > one:
            print(f'Você escolheu a opção maior e menor. O maior número é o {two}, ele está a {two - one} casas '
                  f'decimais de distância.')
            sleep(4.5)
            options = None
        else:
            print(f'Você escolheu a opção maior e menor. Não há maior nem menor entre esses números, ambos são iguais '
                  f'não há casas decimais de distância.')
            sleep(4.5)
            options = None
    elif options == 4:
        one = float(input('Você escolheu a opção de digitar novos números.\n\033[5:30mDigite o primeiro número: '))
        two = float(input('\033[5:30mDigite o segundo número: '))
        sleep(2.5)
        options = None
    else:
        print('Foi um prazer, você selecionou a opção referente ao encerramento do programa e assim será feito.\n'
              'Até a próxima!')
