#  Programa que lê um número inteiro, pergunta qual será a base de conversão e o converte devidamente para a opção
#  escolhida pelo usuário.

number = int(input('Programa que converte números, por favor escolha que tipo de conversão deseja fazer:\n\n'
                   '1. Binário.\n'
                   '2. Octal.\n'
                   '3. Hexadecimal.\n'
                   '0. Encerrar Programa.\n'
                   '\nDigite um número referente a opção: '))

while number < 0 or number > 3:
    print('Erro! O número digitado deve estar entre as opções, por favor releia as suas opções e selecione apenas'
          ' uma opção existente.\n\n'
          '1. Binário.\n'
          '2. Octal.\n'
          '3. Hexadecimal.\n'
          '0. Encerrar Programa.\n')

    number = int(input('Digite um número referente a opção: '))

if number == 0:
    print('Obrigado por utilizar nossos serviços, fim do programa.')

if number == 1:
    binario = int(input('Digite um número inteiro para conversão: '))
    print(bin(binario))

if number == 2:
    octal = int(input('Digite um número inteiro para conversão: '))
    print(oct(octal))

if number == 3:
    hexadecimal = int(input('Digite um número inteiro para conversão: '))
    print(hex(hexadecimal))
