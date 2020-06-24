#  Segunda versão de uma progressão aritimética utilizando o while ao invés do for.

first_term = int(input('\033[5:32mQual é o primeiro termo desta PA?\n\033[5:30mResposta: '))
reason = int(input('\033[5:32mQual é a razão desta PA?\n\033[5:30mResposta: '))
termos = 10  # int(input('\033[5:32mQuantos termos você quer mostrar?\n\033[5:30mResposta: '))

while termos != 0:

    if termos > 1:
        print(first_term, end=', ')
    else:
        print(first_term)

    first_term += reason
    termos -= 1
