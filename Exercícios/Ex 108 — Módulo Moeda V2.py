#  Segunda versão do programa utilizando módulos.
from modulos import moeda_two

money = float(input('Quanto dinheiro você possui?\nResposta: '))

print(f'O dobro de {moeda_two.dobro(money, formatado=True)}\nA metade é igual a: '
      f'{moeda_two.metade(money, formatado=True)}\nCom dez porcento de aumento fica: '
      f'{moeda_two.aumento(money, 10, formatado=True)}\nCom vinte porcento de desconto fica: '
      f'{moeda_two.desconto(money, 20, formatado=True)}')
