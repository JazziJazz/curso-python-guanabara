#  Programa que lê vários números e os adiciona em uma lista, ao final, monta uma nova lista com os números pares e
#  os números impares.

lista = []
lista_pares = []
lista_impares = []

while True:
    number = input(f'\033[5:35mDigite um número, iremos adiciona-lo em uma lista: ').strip()

    if number.isdigit() is False and number[1:].isdigit() is False:
        for pares in range(0, len(lista)):
            if (lista[pares] % 2) == 0:
                lista_pares.append(lista[pares])

        for impares in range(0, len(lista)):
            if (lista[impares]) % 2 != 0:
                lista_impares.append(lista[impares])
        break
    else:
        lista.append(int(number))

print(f'\033[5:32mA lista padrão: \033[5:33m{sorted(lista)}\033[5:32m.\n'
      f'\033[5:32mA lista dos impares: \033[5:33m{sorted(lista_impares)}\033[5:32m.\n'
      f'\033[5:32mA lista dos pares: \033[5:33m{sorted(lista_pares)}\033[5:32m.')
