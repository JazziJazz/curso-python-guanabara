#  Programa que lê o salário de uma pessoa, pergunta o valor do imóvel que ela deseja comprar, quantos anos deseja
#  pagar e exibe na tela se o financiamento foi aprovado ou não, não podendo exceder trinta porcento do salário.

house = float(input('Qual é o valor total da residência?\nRESPOSTA: '))
money = float(input('Qual é sua renda mensal?\nRESPOSTA: '))
years = int(input('Em quantos anos você deseja pagar esse financiamento?\nRESPOSTA: '))

if (house / (years * 12)) > (money - (30 * money / 100.0)):
    print('Empréstimo negado.')
else:
    print(f'Empréstimo aprovado! O valor de sua parcela ficará em R${house / (years * 12):.2f}.')
