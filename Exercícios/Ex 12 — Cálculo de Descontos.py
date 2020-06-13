# Programa que lê o valor de um produto e aplica um desconto de cinco porcento sobre o valor total.

produto = float(input('Digite o valor do produto: '))
desconto = (produto - (5 * produto / 100.0))

print(f'O valor do produto original é de R${produto:.2f}.\nCom o desconto de cinco porcento vai para o preço total de R${desconto:.2f}.')
