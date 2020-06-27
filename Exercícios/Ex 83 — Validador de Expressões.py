
expression = input('\033[5:33mDigite uma expressão, verificaremos se ela é válida: ')
parenteses_esquerda = 0
parenteses_direita = 0

for parenteses in range(0, len(expression)):
    if expression[parenteses] == '(':
        parenteses_esquerda += 1
    elif expression[parenteses] == ')':
        parenteses_direita += 1

if parenteses_esquerda == parenteses_direita:
    print(f'A expressão: \033[5:35m{expression} \033[5:33mé valida.')
else:
    print(f'A expressão: \033[5:31m{expression} \033[5:33mé invalida.')
