#  Programa simples que faz uma contagem regressiva começando do maior número para o menor.
from time import sleep

for i in range(10, -1, -1):
    sleep(1)
    print(f'É {i}.')

print('Fim do programa.')
