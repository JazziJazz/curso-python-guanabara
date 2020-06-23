#  Programa que lê o peso de determinado número de pessoas e exibe na tela qual é o maior peso deste grupo, e o menor.

quantidade_pessoas = int(input('Digite a quantidade de pessoas nesse grupo\nResposta: '))
menor = None
maior = None

for i in range(1, quantidade_pessoas + 1):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))

    if menor is None or (peso < menor):
        menor = peso
    if maior is None or (peso > maior):
        maior = peso

print(f'O MAIOR peso deste grupo é de: {maior:.2f}.\nO MENOR peso é de: {menor:.2f}.')
