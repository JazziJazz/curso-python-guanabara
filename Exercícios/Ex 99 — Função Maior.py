#  Programa que recebe vários parametros e analisa quantos valores foram passados e qual deles é o maior.


def maior(* numbers):
    count_numbers = 0
    hig = None

    for n in numbers:
        if hig is None or n > hig:
            hig = n
        count_numbers += 1

    print(f'Houve um total de {count_numbers} números.\nO maior número é o: {hig}.')


maior(5, 5, 2, 3, 1, 25, 100, 2234, 10, 3, 0, 1234)
