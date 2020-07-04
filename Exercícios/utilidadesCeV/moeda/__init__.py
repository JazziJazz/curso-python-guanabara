#  Módulos úteis contendo funções para realização de cálculos e outros.


def dobro(n, formatado=False):
    if formatado:
        return f'R$ {n * 2:.2f}'
    return n * 2


def metade(n, formatado=False):
    if formatado:
        return f'R$ {n / 2:.2f}'
    return n / 2


def aumento(n, porcento, formatado=False):
    if formatado:
        return f'R$ {(n + (porcento * n / 100.0)):.2f}'
    return n + (porcento * n) / 100.0


def desconto(n, porcento, formatado=False):
    if formatado:
        return f'R$ {(n - (porcento * n) / 100.0):.2f}'
    return n - ((porcento * n) / 100.0)


def resumo(n, porcento_aumento, porcento_desconto):
    return f'O preço analisado é igual a: \t\tR${n:.2f}\nO dobro do preço é igual a: \t\tR${dobro(n):.2f}\nA metade do' \
           f' preço é igual a: \t\tR${metade(n):.2f}\nE o preço com o aumento de {porcento_aumento}% fica em: ' \
           f'\tR${aumento(n, porcento_aumento):.2f}\nPor último, com desconto de {porcento_aumento}% fica em: ' \
           f'\tR${desconto(n, porcento_desconto):.2f}'
