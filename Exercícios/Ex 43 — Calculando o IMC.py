#  Programa que exibe o cálculo do IMC e exibe na tela o resultado para a pessoa e algumas instruções.

peso = float(input('Digite aqui o seu peso: '))
altura = float(input('Digite aqui sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Você tem o IMC de {imc:.2f}, você está abaixo do seu peso. Procure já um nutricionista pois isso pode '
          f'representar um problema sério de saúde.')
elif imc < 25:
    print(f'Continue assim! Você tem o IMC de {imc:.2f} e está em seu peso ideal. Mantenha essa boa rotina que sua'
          f' saúde e bem estar sempre vão estar em dia.')
elif imc < 30:
    print(f'Poxa, você está com sobrepeso! Isso pode significar que você pode ter diversos problemas de saúde, '
          f'cuide-se mais, valorize a vida. O seu IMC é de {imc:.2f}.')
elif imc < 40:
    print(f'Você está obeso. É infeliz, uma condição que afeta a qualidade de vida de milhões de humanos por todo'
          f' o planeta Terra. Você precisa se cuidar com urgência, pois isso pode significar uma má qualidade de vida'
          f' além de uma péssima saúde.')
else:
    print(f'Você tem obesidade mórbida. Procure um hospital e entre na fila de cirurgia, valorize a vida. Seu IMC é'
          f' de {imc:.2f}.')
