#  Programa que simula um caixa eletrônico, pergunta quanto dinheiro a pessoa quer sacar. Devolve ela um resultado em
#  cédulas até atingir aquele valor.

money = int(input('\033[5:32mDigite a quantidade de dinheiro a ser sacada: '))
cedula = 50
total_de_cedulas = 0

while True:
    if money >= cedula:
        money -= cedula
        total_de_cedulas += 1
    else:
        if total_de_cedulas > 0:
            print(f'\033[5:36mVocê receberá um total de:\033[5:32m {total_de_cedulas} notas de R${cedula:.2f}.')

        if cedula == 50:
            cedula = 20
            total_de_cedulas = 0
        elif cedula == 20:
            cedula = 10
            total_de_cedulas = 0
        else:
            cedula = 1
            total_de_cedulas = 0

        if money == 0:
            break
