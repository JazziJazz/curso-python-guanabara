#  Programa que exibe quantas casas de unidades, dezenas, centenas e milhares um número possui.

number = int(input('Digite seu número: '))

print(f'\nEstamos analisando o número: {number}.\n'
      f'Nesse mesmo número há: {number // 1 % 10} unidade(s).\n'
      f'Nesse mesmo número há: {number // 10 % 10} dezena(s).\n'
      f'Nesse mesmo número há: {number // 100 % 10} centena(s).\n'
      f'Nesse mesmo número há: {number // 1000 % 10} milhar(es).\n'
      f'Fim do programa.')
