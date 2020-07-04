#  Programa que exibe informações sobre as funções nativas do Python. Quando o usuário digita 'FIM' o programa se
#  encerra.


def custom_input(string):
    print(f'\n{(len(string) + 4) * "~"}')
    print(f'  {string}')
    print(f'{(len(string) + 4) * "~"}')


while True:
    question = input(f'\033[5:35mDigite uma função, exibiremos as informações desta para você: ')

    if question.upper() == 'FIM':
        custom_input('Programa encerrado, foi um prazer.')
        break
    else:
        help(question)
