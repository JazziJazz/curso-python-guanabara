#  Terceira edição do programa de módulos.
from modulos import moeda_two

money = float(input('Digite quanto dinheiro você possui.\nResposta: '))
print(moeda_two.resumo(money, 10, 10))
