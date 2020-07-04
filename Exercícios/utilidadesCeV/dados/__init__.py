def leia_dinheiro(string):
    money = input(f'{string}')
    while money.isdigit() is False and money[1:].isdigit() is False:
        money = input(f'\033[5:31mErro! O valor {money} é inválido, tente novamente.\n\033[mDigite um valor '
                      f'monetário: ')
    return float(money)

