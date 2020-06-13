# Programa que calcula o valor total a pagar por um veículo considerando os dias que o veículo permaneceu alugado e a quilometragem rodada.

days = int(input('Quantos dias você ficou com o veículo?: '))
km = int(input('Quantos quilometros você rodou com o veículo?: '))

calculo_days = days * 60
calculo_km = km * 0.15

print(f'\nVocê deve um total de R${calculo_days:.2f} referente aos dias de aluguel.\nVocê deve um total de {calculo_km:.2f} referente a quilometragem rodada, portanto você deve a locadora um total de R${calculo_days + calculo_km:.2f}.')
