#  Programa que lê seis números inteiros e se eles forem pares some eles com os outros pares.

soma = 0

for i in range(1, 7):
    number = int(input('Digite um número: '))

    if number % 2 == 0:
        soma += number

print(soma)
