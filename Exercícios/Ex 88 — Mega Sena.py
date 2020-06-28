#  Programa que palpita sobre jogos da Mega Sena. O número não pode existir na tabela.
from random import randint
from time import sleep

mega_sena = []
quantidade_jogos = int(input('Quantos jogos você deseja gerar?: '))

for i in range(0, quantidade_jogos):
    for numeros in range(0, 6):
        random_number = randint(0, 60)

        while random_number in mega_sena:
            random_number = randint(0, 60)

        mega_sena.append(random_number)
    print(f'Gerando jogo {i + 1}: {mega_sena}')
    sleep(1.5)
    mega_sena.clear()
