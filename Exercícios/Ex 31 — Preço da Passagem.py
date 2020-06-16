#  Programa que verifica qual é a distância de uma viagem pretendida, efetua o calcudo do valor da passagem com
#  base na distância desta mesma viagem.

distance = float(input('Quantos quilometros tem a sua viagem?\nRESPOSTA: '))
price = [distance * 0.50, distance * 0.45]

if distance > 200:
    print(f'Você deverá pagar o valor de R${price[1]:.2f} pela sua passagem.')
else:
    print(f'A sua passagem não tem desconto, portanto você deverá pagar o valor de R${price[0]:.2f}.')
