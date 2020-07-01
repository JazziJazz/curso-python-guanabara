from random import shuffle


def sorteia(listagem):
    shuffle(listagem)
    new_list = []

    for i in range(0, 5):
        new_list.append(listagem[i])

    return sorted(new_list)


def soma_par(listagem):
    new_list = []

    for pares in listagem:
        if (pares % 2) == 0:
            new_list.append(pares)
    return sorted(new_list)


lista = [78, 86, 85, 4, 0, 30, 88, 19, 54, 42]

random = sorteia(lista)
soma_pares = soma_par(lista)
ambos = soma_par(random)

print(f'Os cinco elementos sorteados na lista são: {random}.\nOs números pares nessa lista são: {soma_pares}.\n'
      f'Os pares dentro da lista dos cinco elementos sorteados são iguais a: {ambos}.')
