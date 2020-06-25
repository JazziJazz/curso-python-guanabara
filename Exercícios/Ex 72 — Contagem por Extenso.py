#  Programa que pede a entrada de um número entre zero e vinte e quando digitado exibe o mesmo só que digitado por
#  extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
pergunta = int(input('\033[5:32mDigite um número, nós iremos exibi-lo na tela.\n\033[5:30mNúmero: '))

while pergunta < 0 or pergunta > 20:
    pergunta = int(input('\033[5:31mErro! Você digitou um número inválido, só são tolerados números entre zero e vinte.'
                         '\n\033[5:32mDigite um número, nós iremos exibi-lo na tela.\n\033[5:30mNúmero: '))

print(f'\033[5:33mO número que você digitou, por extenso é igual a:\033[5:36m {numeros[pergunta]}.')
