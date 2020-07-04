#  Programa que só permite a leitura de um número se este for um inteiro, se for qualquer coisa diferente disso, então
#  retornará uma mensagem de erro e pedirá para que o valor digitado seja válido, ou seja, um inteiro.


def lendo_inteiros(num):
    while num.isdigit() is False and num[1:].isdigit() is False:
        num = input('\033[5:31mErro! Valor digitado inválido, tente novamente.\n\033[5:32mDigite um número: ')
    return int(num)


number = lendo_inteiros(input('Digite um número: '))
print(number)