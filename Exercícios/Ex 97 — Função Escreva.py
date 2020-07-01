#  Programa que chama uma função para escrever algo para você formatado devidamente "bonitinho".


def escreva(string):
    print(f'{(len(string) + 4) * "~"}')
    print(f'  {string}')
    print(f'{(len(string) + 4) * "~"}')


escreva('Olá, mundo!')

