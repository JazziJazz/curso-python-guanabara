# Programa que lê a quantidade de real a ser convertida a dollar.

money = float(input('Quantos reais você tem?: '))
print(f'Com R${money} você pode comprar até um total de ${money / 4.82:.2f}.')
