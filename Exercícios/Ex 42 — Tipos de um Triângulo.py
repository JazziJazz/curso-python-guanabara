#  Programa que verifica se os ângulos podem formar um triângulo e exibe na tela que tipo de triângulo seria formado
#  com a existência dos lados informados.

lado_a = float(input('Digite o valor do lado A de um triângulo: '))
lado_b = float(input('Digite o valor do lado B de um triângulo: '))
lado_c = float(input('Digite o valor do lado C de um triângulo: '))

if (lado_b - lado_c) < lado_a < (lado_b + lado_c) and \
        (lado_a - lado_c) < lado_b < (lado_a + lado_c) and \
        (lado_a - lado_b) < lado_c < (lado_a + lado_b):

    if lado_a == lado_b and lado_b == lado_c:
        print('O triângulo poderia ser formado, ele seria do tipo Equilátero.')
    elif lado_a != lado_b and lado_b != lado_c and lado_a != lado_c:
        print('O triângulo poderia ser formado, ele seria do tipo Escaleno.')
    elif lado_a == lado_b or lado_a == lado_c and lado_a != lado_b or lado_c:
        print('O triângulo poderia ser formado, ele seria do tipo Isósceles.')

else:
    print('Este triângulo não poderia nunca ser formado.')
