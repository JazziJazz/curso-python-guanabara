#  Programa que lê três números, exibe qual é o maior e o menos entre esses.

menor = None
maior = None

for i in range(0, 3):
    number = int(input(f'Digite o {i + 1} número: '))

    if menor is None:
        menor = number
    else:
        if number < menor:
            menor = number

    if maior is None:
        maior = number
    else:
        if number > maior:
            maior = number

print(f'O maior número é o: {maior}. O menor número é o {menor}.')
