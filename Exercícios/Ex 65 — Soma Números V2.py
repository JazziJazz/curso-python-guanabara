#  Programa que lê vários números, e ao término do programa exibe na tela a média entre esses números, a soma, quantos
#  números foram digitados e o maior e menor valor entre eles.

funcionando = True
maior = None
menor = None

cont = 0
soma = 0
media = 0

while funcionando is True:
    number = float(input('\033[5:34mDigite um número, o programa faz várias coisas interessantes.\n\033[5:30mNúmero: '))

    cont += 1
    soma += number
    media = soma / cont

    pergunta = input('\033[5:34mVocê deseja continuar? [S/N]\n\033[5:30mResposta: ').strip().upper()

    if menor is None or (number < menor):
        menor = number
    if maior is None or (number > maior):
        maior = number

    while pergunta in 'S':
        number = float(
            input('\033[5:34mDigite um número, o programa faz várias coisas interessantes.\n\033[5:30mNúmero: '))

        cont += 1
        soma += number
        media = soma / cont

        pergunta = input('\033[5:34mVocê deseja continuar? [S/N]\n\033[5:30mResposta: ').strip().upper()

        if menor is None or (number < menor):
            menor = number
        if maior is None or (number > maior):
            maior = number

    while pergunta not in 'S' and pergunta not in 'N':
        pergunta = input('\033[5:31mErro! Só há duas respostas válidas para essa questão, releia atentamente a '
                         'pergunta.\n\033[5:34mVocê deseja continuar? [S/N]\n\033[5:30mResposta: ').strip().upper()

    if pergunta in 'N':
        funcionando = False

print(f'\033[5:32mVocê digitou {cont} números.\nO maior número digitado é o: {maior}. O menor número digitado é o: '
      f'{menor}.\nA soma entre esses números é de: {soma}. A média entre esses números é de: {media}.')
