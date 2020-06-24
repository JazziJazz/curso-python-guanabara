#  Programa que lê o nome e o sexo de uma pessoa, mas não aceita nenhuma resposta diferente de M ou F para o sexo.

name = input('Digite o seu nome: ').strip().title()
sex = input('Qual o seu sexo? [M/F]: ').strip().upper()  # [0] pega somente a primeira letra.

while len(sex) > 1:
    sex = input(f'\033[31mVocê está digitando mais que uma letra. As únicas respostas disponíveis são masculino (M) ou '
                f'feminino (F). \n\033[1:33mQual é o seu sexo? [M/F]: ').strip().upper()

    while sex not in 'M' and sex not in 'F':
        sex = input(f'\033[31mResposta inválida, por favor. As únicas respostas disponíveis são masculino (M) ou '
                    f'feminino (F). \n\033[1:33mQual é o seu sexo? [M/F]: ').strip().upper()

print(f'\033[3:34mVocê é {name} e é do sexo {sex}.')
