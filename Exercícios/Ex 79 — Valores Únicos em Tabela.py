#  Programa que adiciona vários números dentro de uma tabela ao gosto do usuário, se o número já existir dentro da
#  tabela, então ele exibirá uma mensagem informando ao usuário que o número está duplicado e não irá adiciona-lo. Caso
#  o usuário digite um número negativo, o programa se encerra.

lista = []

while True:
    number = input('\033[5:36mDigite um número, iremos adiciona-lo a tabela: ')

    while number[1:].isnumeric() is False:
        number = input('\033[5:31mErro! Apenas números são permitidos.\n\033[5:36mDigite um número, iremos adiciona-lo '
                       'a tabela: ')

    while int(number) in lista:
        number = input('\033[5:31mErro! Esse número já foi adicionado a tabela.\n\033[5:36mDigite um número, '
                       'iremos adiciona-lo a tabela: ')

    if int(number) < 0:
        lista.sort()
        break

    lista.append(int(number))

print(f'A lista dos números informados por você será exibida logo abaixo:\n\033[5:33m{lista}')
