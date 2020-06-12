# Programa que lê uma variável e imprime na tela todas as informações sobre ela.

variavel = input('Digite alguma coisa: ')

print(f'A variável é um dígito?: {variavel.isdigit()}\n'
    f'A variável é alfa-numérica?: {variavel.isalpha()}\n'
    f'A variável é um número?: {variavel}\n'
    f'A variável só tem espaços?: {variavel.isspace()}\n'
    f'A variável está toda em maiúsculo?: {variavel.isupper()}\n'
    f'A variável está toda em minusculo?: {variavel.islower()}\n'
    f'A variável é um título?: {variavel.istitle()}')