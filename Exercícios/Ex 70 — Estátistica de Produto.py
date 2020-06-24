#  Programa que lê o nome e o preço de vários produtos. Ao final exibe na tela o total gasto na compra, o produto mais
#  barato e o seu valor e quantos produtos com preço superior a R$1.000 foram comprados.

mais_barato = None
nome_mais_barato = None
produto_caro = 0
total_gasto = 0
quantidade_produtos = 0

print('Programa de análise de dados de compras. Utilizar com carinho.')

while True:
    name = input('\033[5:35mQual é o nome do produto?\n\033[5:30mResposta: ').title().strip()
    price = float(input('\033[5:35mDigite a idade desta pessoa: '))

    if mais_barato is None or price < mais_barato:
        mais_barato = price
        nome_mais_barato = name

    if price >= 1000:
        produto_caro += 1

    total_gasto += price
    quantidade_produtos += 1

    pergunta = input('\033[5:30mDeseja continuar? [S/N]: ').strip().upper()

    while pergunta not in 'S' and pergunta not in 'N':
        pergunta = input('\033[5:31mErro! Atenção no que digita! O programa só aceita as respostas sim ou não.\n'
                         '\033[5:30mDeseja continuar? [S/N]: ')

    if pergunta == 'N':
        print(f'Boa-compra, volte sempre. Você gastou um total de: R${total_gasto:.2f}. Você comprou um total de: '
              f'{quantidade_produtos}.\nO produto mais barato foi o: {nome_mais_barato}, você pagou R${mais_barato:.2f}'
              f'. Ao total houveram: {produto_caro} produtos com um preço superior a mil R$.\n\n\033[5:36mBye-Bye!')
        break
