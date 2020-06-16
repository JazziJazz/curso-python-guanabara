#  Programa que executa uma veirificação do primeiro e último nome de uma pessoa e lhe dá saudações.

name = input('Qual é o seu nome completo?\nRESPOSTA: ').strip().title().split()

print(f'Seja-bem vindo. A sua reserva neste hotel se aproxima do fim, foi um prazer ter você em nosso '
      f'estabelecimento.\nAté mais senhor(a): {name[0], name[-1]}.')
