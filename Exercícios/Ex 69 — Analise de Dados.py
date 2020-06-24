#  Programa de cadastramento de pessoas. Lê a idade e o sexo de várias pessoas, a cada nova pessoa perguntada o programa
#  pergunta ao usuário se ele deseja continuar. Quando ele não desejar continuar, ira imprimir na tela quantas mulheres
#  cadastradas tem menos de vinte anos, quantos homens foram cadastrados e quantas pessoas maiores de dezoitos anos há.

print(52 * '———')
print('Programa de Cadastramento de Pessoas: ')
print(52 * '———')

maiores = 0
mulheres_menores = 0
homens = 0
pessoas = 0

while True:
    idade = input('\033[5:35mDigite a idade desta pessoa: ')

    while type(idade) != int:
        idade = int(input('\033[5:31mErro! Atenção ao utilizar o cadastramento, só é permitido números inteiros.\n'
                          '\033[5:35mDigite a idade desta pessoa: '))

    sexo = input('\033[5:35mQual é o sexo dessa pessoa? [M/F]\n\033[5:30mResposta: ').strip().upper()

    while sexo not in 'M' and sexo not in 'F':
        sexo = input('\033[5:31mErro! Atenção ao utilizar o cadastramento, só é permitido o uso do sexo masculino ou '
                     'feminino.\n\033[5:35mQual é o sexo dessa pessoa? [M/F]\n\033[5:30mResposta: ').strip().upper()
    pessoas += 1

    if idade >= 18:
        maiores += 1

    if sexo == 'M':
        homens += 1
    else:
        if idade < 20:
            mulheres_menores += 1

    pergunta = input('\033[1:36mVocê deseja continuar? [S/N]\n\033[5:30mResposta: ').strip().upper()

    if pergunta == 'N':
        print(f'Há um total de: {pessoas} cadastradas no sistema.\nHá um total de: {homens} homens cadastrados.\n'
              f'Há {maiores} pessoas maiores de idade. Há um total de {mulheres_menores} mulheres com menos de vinte '
              f'anos de idade.')
        break
