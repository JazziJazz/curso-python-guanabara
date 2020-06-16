#  Programa que lê um número e se for o que a máquina sorteou então o jogador vence, se não, ele perde.
from random import randint

number = int(input(
    'Eu vou pensar em um número, será que você consegue acertar?\nDe um a cinco, que número eu pensei?\nRESPOSTA: '))
random = randint(0, 5)
vezes = 1

while number != random:
    vezes += 1
    number = int(input(f'Que pena, você errou. Tente até acertar!\nNúmero: '))

print(f'Meus parabéns! Você é realmente muito bom, conseguiu acertar o número na: {vezes} vez.\nFoi realmente um '
      f'ótimo jogo, eu me diverti muito. Até a proxima!')
