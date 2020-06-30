dados = {}
pessoas = []
total_pessoas = 0
soma_idade = 0

while True:
    dados['nome'] = input(f'Qual é o nome da {total_pessoas + 1} pessoa?: ')
    dados['idade'] = int(input('Qual é a idade dessa pessoa?: '))
    dados['sexo'] = input('Essa pessoa é do sexo masculino ou feminino? [M/F]: ').upper().strip()

    while dados['sexo'] not in 'M' and dados['sexo'] not in 'F':
        dados['sexo'] = input('Essa pessoa é do sexo masculino ou feminino? [M/F]: ').upper().strip()

    soma_idade += dados['idade']
    pessoas.append(dados.copy())
    #  dados.clear() não é necessário, pois a cada vez que o loop é efetuado os dados são alterados.
    total_pessoas += 1

    pergunta = input('Você deseja continuar o cadastramento de pessoas? [S/N]: ').upper().strip()

    while pergunta not in 'S' and pergunta not in 'N':
        pergunta = input('\033[5:31m Erro! Só há duas respostas, sim ou não.\n\033[5:30m Você deseja continuar o '
                         'cadastramento de pessoas? [S/N]: ').upper().strip()

    if pergunta == 'N':
        print(f'O total de pessoas cadastradas foi: {total_pessoas}.\nA média de idade desse grupo de pessoas é: '
              f'{soma_idade / total_pessoas:.2f}.')

        lista_mulheres = []
        lista_pessoas_acima_media = []

        for k in range(0, len(pessoas)):
            if pessoas[k]['sexo'] == 'F':
                lista_mulheres.append(pessoas[k]['nome'])

            if pessoas[k]['idade'] >= (soma_idade / total_pessoas):
                lista_pessoas_acima_media.append(pessoas[k]['nome'])

        print(f'As mulheres cadastradas são: {sorted(lista_mulheres)}.\nAs pessoas com idade acima da média são: '
              f'{sorted(lista_pessoas_acima_media)}.')
        break
