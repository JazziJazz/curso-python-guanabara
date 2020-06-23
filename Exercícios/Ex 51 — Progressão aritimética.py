#  Programa que lê o primeiro termo de uma progressão aritmética e o seu termo, executa os dez primeiros termos
#  desta progressão e o imprime na tela.

first_term = int(input('Qual é o primeiro termo dessa PA?\nResposta: '))
razao = int(input('Qual é a razão desta progressão aritmética?\nResposta: '))

for i in range(1, 11):
    print(f'{first_term}', end=' → ')
    first_term += razao

print('ACABOU!')
