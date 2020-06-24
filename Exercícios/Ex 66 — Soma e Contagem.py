#  Programa que lê números inteiros, vai contando quantos números foram digitados e qual é a soma entre eles. Se o
#  número digitado for 999 então, vai parar o programa e exibir na tela os resultados e a despedida.

contador = 0
soma = 0

while True:
    number = int(input('Digite um número (999 para parar): '))

    if number != 999:
        soma += number
        contador += 1
    else:
        break

print(f'Ao total você digitou {contador} números.\nA soma entre eles é de: {soma}.')
