#  Programa que pergunta vários números, exibe a tabuada referente ao número digitado, porém, se o número for negativo
#  o programa é parado, exibindo uma despedida e finalizando a operação.

tabuada_numero = 1

while True:
    number = int(input('\033[5:35mDigite um número, exibiremos a tabuada deste número. Fique atento, um número negativo'
                       ' representa o encerramento do programa.\n\033[5:30mNúmero: '))

    if number > 0:
        while tabuada_numero <= 10:
            print(f'\033[1:32m{number} x {tabuada_numero} = {number * tabuada_numero}.')
            tabuada_numero += 1
        tabuada_numero = 1
    else:
        print(f'\033[5:36mVocê digitou {number}. Isso representa o fim do programa.\nAté mais!')
        break
