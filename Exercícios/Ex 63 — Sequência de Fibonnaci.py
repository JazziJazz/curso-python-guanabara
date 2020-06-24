#  Programa que pergunta quantos termos de uma sequência fibonacci o usuário deseja exibir na tela. Os exibe, pergunta
#  se deseja mostrar mais, se não desejar encerra o programa.

terms = int(input('\033[5:35mQuantos termos desta sequência de Fibonacci você deseja exibir?\n\033[5:30mResposta: '))
first_term = 0
secundary_term = 1

print(f'0, 1', end=', ')

while (terms - 2) != 0:
    tertiary_term = (first_term + secundary_term)

    if terms > 3:
        print(tertiary_term, end=', ')
    else:
        print(tertiary_term, end='.')

    first_term = secundary_term
    secundary_term = tertiary_term

    terms -= 1
