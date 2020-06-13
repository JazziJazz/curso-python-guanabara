# Programa que lê a largua e a altura de uma parede, calcula sua área e a quantidade de tinta a ser utilizada para pinta-la.

altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))

calculo = (altura * largura) / 2

print(f'A área da sua parede é de: {altura * largura:.2f}.\nPara pinta-la será necessário {calculo:.2f} litros de tinta.')
