#  Programa que dá diversas formas de pagamento, baseado na escolha do cliente aplica descontos ou juros.

valor = float(input('Qual é o valor do produto?\nResposta: '))
pagamento = int(input('Escolha sua forma de pagamento:\n\n'
                      '1. À vista no dinheiro.\n'
                      '2. À vista no cartão.\n'
                      '3. Em até duas vezes no cartão.\n'
                      '4. Acima de três vezes no cartão.\n\n'
                      'Resposta: '))

while pagamento < 1 or pagamento > 4:
    print("Erro, opção inválida. Verifique o que você digitou e tente novamente:\n\n"
          "1. À vista no dinheiro.\n"
          "2. À vista no cartão.\n"
          "3. Em até duas vezes no cartão.\n"
          "4. Acima de três vezes no cartão.\n")

    pagamento = int(input('Resposta: '))

if pagamento == 1:
    print('Você escolheu a opção à vista no dinheiro! Portanto, você terá um desconto de dez porcento no valor total!'
          f'O seu produto sem desconto iria sair por R${valor:.2f}. Agora você paga: R${valor - (10 * valor / 100)}.')
elif pagamento == 2:
    print('Você escolheu a opção à vista no cartão! Portanto, você terá um desconto de cinco porcento no valor total!'
          f'O seu produto sem desconto iria sair por R${valor:.2f}. Agora você paga: R${valor - (5 * valor / 100)}.')
elif pagamento == 3:
    print(f'Você escolheu a opção de pagamento em até duas vezes no cartão. O valor a ser pago é de: R${valor:.2f}.')
elif pagamento == 4:
    print('Você decidiu parcelar em até três vezes OU mais no cartão de crédito, um juros de vinte porcento será '
          f'aplicado. O valor original do produto é de R${valor:.2f}. Você deverá pagar um total de: '
          f'{valor + (20 * valor / 100.0)}.')
