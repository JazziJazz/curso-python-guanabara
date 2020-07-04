#  Programa que lê valores, se e somente se forem números.
from utilidadesCeV import dados, moeda

money = dados.leia_dinheiro('Digite um valor monetário: R$')
print(moeda.resumo(money, 10, 10))
