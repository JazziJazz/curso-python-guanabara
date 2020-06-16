# Programa que lê a velocidade que um carro está trafegando e faz uma verificação para decidir se multa, ou não.

velocidade = int(input('Em que velocidade você está trafegando?\nRESPOSTA: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f'MULTADO! Você está trafegando acima do limite de velocidade permitido.\n'
          f'Deverá pagar uma multa no valor de R${multa:.2f}.')
else:
    print('Tenha um bom dia, siga sempre o limite de velocidade e lembre-se; Se beber, não dirija.')
