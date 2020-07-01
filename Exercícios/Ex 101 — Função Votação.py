from datetime import datetime


def voto(x):
    if (datetime.today().year - x) < 16:
        return print('Não possui idade mínima para voto.')
    elif (datetime.today().year - x) < 18:
        return print('O voto é opcional.')
    else:
        return print('O voto é obrigatório.')


voto(1998)
