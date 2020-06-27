#  Programa que lê vários números, ao final exibe a lista de ordem decrescente e se há o número cinco nela, e quantos
#  números foram adicionados nela.

lista = []
numeros = 0
numero_valor = 5

while True:
    number = input(f'\033[5:35mDigite um número, iremos adiciona-lo em uma lista: ').strip()

    if number[1:].isdigit() is False and number.isdigit() is False:
        break
    else:
        lista.append(int(number))
        numeros += 1

if 5 in lista:
    print(f'Você digitou um total de: {numeros} números.\nA lista exibida de forma ordenada de maneira decrescente: '
          f'{sorted(lista, reverse=True)}\nO valor: {numero_valor} está presente na lista.')
else:
    print(f'Você digitou um total de: {numeros} números.\nA lista exibida de forma ordenada de maneira decrescente: '
          f'{sorted(lista, reverse=True)}\nO valor: {numero_valor} não está presente na lista.')
