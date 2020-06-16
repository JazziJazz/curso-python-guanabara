#  Programa que lê um ano inteiro e exibe na tela se este mesmo ano é bisexto ou não.

year = int(input('Qual ano você quer saber se é bisexto?\nDigite o ano: '))
bisexto = year % 4

if bisexto == 0:
    print(f'O ano que você digitou: {year} é bisexto.')
else:
    print(f'O ano de {year} não é um ano bisexto.')
