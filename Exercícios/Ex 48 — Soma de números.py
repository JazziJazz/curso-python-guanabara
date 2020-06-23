#  Programa que soma todos os números impares múltiplos de três em um intervalo de zero a quinhentos.

soma = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i

print(f'A soma total dos números impares em um intervalo de um a quinhentos é igual a: {soma}.')
