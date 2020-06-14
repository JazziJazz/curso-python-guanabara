# Programa que lê o nome de quadro alunos e os salva em uma lista, além disso sorteia um deles para apagar o quadro.
from random import choice

alunos = []

for i in range(0, 4):
    alunos.append(input('Digite o nome do aluno: '))

print(f'O aluno sorteado é o: {choice(alunos)}.')
