#  Programa que lê um produto seguido por um preço, no final mostre todos os produtos seguidos de seus respectivos
#  preços organizados de forma tabular.

mercado = ('Bolacha Maria', 3.50, 'Trakinas de Limão', 52.40, 'Kinder Ovo', 10,
           'Pão de Forma (KG)', 14.50, 'Carne Bovina', 12.50, 'Salmão Fresco (PEIXE INTEIRO)', 54.90,
           'Rodrigo Siliunas (PORA HORA)', 0.01)

print(f'\033[5:36m{60 * "="}\n\033[5:32m{"MERCADO DO POVO":^60}\n\033[5:36m{60 * "="}\n')

for i in range(0, len(mercado)):
    if i % 2 == 0:
        print(f'\033[0:1:38m{mercado[i]:.<50}', end='')
    else:
        print(f'\033[0:1:32mR${mercado[i]:>7.2f}')

print(f'\n\033[5:36m{60 * "="}')