#  Programa que exibe o valor de uma tabuada.

number = int(input('De qual valor você deseja saber a tabuada?\nResposta: '))

for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')
