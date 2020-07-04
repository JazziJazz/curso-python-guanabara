#  Programa que lê um número inteiro e um número real, apenas se eles forem números desse tipo, caso contrário exiba uma
#  mensagem de erro informando que o valor digitado é inválido.


def leia_inteiro():
    while True:
        try:
            number = int(input('\033[5:35mDigite um número inteiro: \033[m'))
        except (TypeError, ValueError):
            print(f'\033[5:31mERRO: A entrada é invalida. Somente números são permitidos.\n')
            continue
        except KeyboardInterrupt:
            print('\033[5:31mEntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return number


def leia_real():
    while True:
        try:
            num = float(input('\033[5:36mDigite um número real: \033[m'))
        except (TypeError, ValueError):
            print(f'\033[5:31mERRO: A entrada é invalida. Somente números reais são permitidos.\n')
            continue
        except KeyboardInterrupt:
            print('\033[5:31mEntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return num


numero = leia_inteiro()
print(numero, type(numero))

num_real = leia_real()
print(num_real, type(num_real))
