#  Programa que verifica se é possível formar um triângulo. Se for, então imprime na tela que é possível, se não
#  imprime na tela que não é possível.

triangulo = [float(input('Qual é o tamanho da primeira reta do triângulo?: ')),
             float(input('Qual é o tamanho da segunda reta do triângulo?: ')),
             float(input('Qual é o tamanho da terceira reta do triângulo?: '))
             ]

if (triangulo[1] - triangulo[2]) < (triangulo[0]) < (triangulo[1] + triangulo[2]) and \
        (triangulo[0] - triangulo[2]) < (triangulo[1]) < (triangulo[0] + triangulo[2]) and \
        (triangulo[0] - triangulo[1]) < (triangulo[2]) < (triangulo[0] + triangulo[1]):
    print('O triângulo pode ser formado com sucesso.')
else:
    print('O triângulo não pode ser formado.')
