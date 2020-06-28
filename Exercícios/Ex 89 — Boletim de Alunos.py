#  Programa que lê o nome e duas notas de vários alunos, ao final exibe uma tabela contendo o nome e a média desses
#  alunos, e não encerra o programa. Pergunta se quer que exiba as notas individuais de cada aluno cadastrado, se não,
#  encerra o programa.

lista = []
dados = []
numeros_extenso = ('Primeira', 'Segunda', 'Terceira', 'Quarta', 'Quinta', 'Sexta')
qtd_notas = int(input('Quantas matérias os alunos possuem por semestre?: '))

while 1 > qtd_notas > 6:
    qtd_notas = int(input('Quantas matérias os alunos possuem por semestre? [1..6]: '))

while True:
    media = 0
    dados.append(input('Qual é o nome do aluno?: '))

    for quantidade_notas in range(0, qtd_notas):
        nota = float(input(f'Qual é a {numeros_extenso[quantidade_notas].lower()} nota do aluno?: '))
        media += nota
        dados.append(nota)

    dados.append(media), lista.append(dados[:])
    dados.clear()

    pergunta = input('Você deseja continuar com a adição de alunos? [S/N]: ').strip().upper()

    while pergunta not in 'S' and pergunta not in 'N':
        pergunta = input('Você deseja continuar com a adição de alunos? [S/N]: ')

    if pergunta == 'N':
        print(f'{"=" * 51}\n{"ESCOLA DA PUTARIA":^51}\n{"=" * 51}\n')

        for alunos in range(0, len(lista)):
            print(f'[ID: {alunos:>2}] {lista[alunos][0]:.<30} Média: {lista[alunos][qtd_notas + 1] / qtd_notas:>4.2f}')

        pergunta = int(input('Mostrar as notas de qual aluno? [ID]: '))

        while pergunta != 999:
            print(f'As notas do aluno {lista[pergunta][0]}: ', end='')

            for quantidade_notas in range(1, qtd_notas + 1):
                if quantidade_notas < qtd_notas:
                    print(f'{lista[pergunta][quantidade_notas]}', end=', ')
                else:
                    print(f'{lista[pergunta][quantidade_notas]}', end='.')

            pergunta = int(input('\nMostrar as notas de qual aluno? [ID]: '))

        print(f'Ótimo, você completou mais um desafio. Até a proxima.')
        break
