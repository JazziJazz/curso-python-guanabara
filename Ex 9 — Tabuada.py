# Programa que imprime a tabuada de um número informado pelo usuário.

tabuada = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{tabuada} x {i} = {tabuada * i}.')