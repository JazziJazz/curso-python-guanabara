#  Terceira versão de uma progressão aritmética utilizando o while ao invés do for. Pergunta ao usuário se ele deseja
#  mostrar mais termos, se não desejar encerra o programa.
from time import sleep

first_term = int(input('\033[5:32mQual é o primeiro termo desta PA?\n\033[5:30mResposta: '))
reason = int(input('\033[5:32mQual é a razão desta PA?\n\033[5:30mResposta: '))
termos = int(input('\033[5:32mQuantos termos você quer mostrar?\n\033[5:30mResposta: '))
question = None

while termos != 0 or question is None:

    if termos > 1:
        print(first_term, end=', ')
    else:
        print(first_term, end='.')

    first_term += reason
    termos -= 1

    if termos == 0:
        sleep(2)
        pergunta = int(input('\033[5:34m\nDeseja mostrar mais termos? Se sim, digite o número. Caso não deseje mais '
                             'termos, digite zero.\n\033[5:30mResposta: '))
        if pergunta == 0:
            question = False
            print(f'\033[5:31mPrograma encerrado, foi um prazer. Até a próxima! Bye-bye!')
        else:
            termos = pergunta
