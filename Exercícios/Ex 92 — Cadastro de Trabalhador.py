from datetime import datetime

cadastro_trabalhador = {'nome': input('Qual o nome do trabalhador(a)?: '),
                        'idade': datetime.today().year - int(input('Qual o ano de nascimento do trabalhador(a)?: ')),
                        'ctps': int(input('Qual é o número da CTPS?: '))}


if cadastro_trabalhador['ctps'] != 0:
    cadastro_trabalhador['ano_contratação'] = int(input('Em qual ano foi contratado(a)?: '))
    cadastro_trabalhador['salário'] = float(input('Qual o salário que o trabalhador(a) recebe?: '))
    cadastro_trabalhador['ano_aposentadoria'] = (cadastro_trabalhador['ano_contratação'] + 35) - \
                                                (datetime.today().year - cadastro_trabalhador['idade'])

    print(f'{cadastro_trabalhador}')
    for k, v in cadastro_trabalhador.items():
        print(f'{k} tem o valor de {v}.')
else:
    print(f'{cadastro_trabalhador}')
    for k, v in cadastro_trabalhador.items():
        print(f'{k} tem o valor de {v}.')
