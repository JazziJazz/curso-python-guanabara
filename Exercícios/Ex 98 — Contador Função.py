#  Programa que é um contador.


def contador():
    for i in range(0, 11):
        if i == 0:
            print(f'Realizando a contagem:\n{i}', end=', ')
        elif i == 10:
            print(f'{i}', end='.')
        else:
            print(f'{i}', end=', ')

    for i in range(10, -1, -2):
        if i == 10:
            print(f'\n\nRealizando a contagem:\n{i}', end=', ')
        elif i == 0:
            print(f'{i}', end='.')
        else:
            print(f'{i}', end=', ')

    inicio = int(input('\n\nHora da contagem personalizada!\nQual o início?: '))
    fim = int(input('Qual é o fim?: '))
    passo = int(input('Qual é o passo?: ')).__abs__()

    if passo == 0:
        passo = 1

    print(f'Realizando contagem!\n')

    if inicio > fim:
        for i in range(inicio, fim, -passo):
            if i == fim + 1:
                print(i, end='.')
            else:
                print(i, end=', ')
    else:
        for i in range(inicio, fim + 1, passo):
            if i == fim:
                print(i, end='.')
            else:
                print(i, end=', ')


contador()
