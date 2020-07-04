#  Programa que analisa várias notas, exibe quantas notas foram ao total, a maior, a menor e a média da turma.


def notas(*notes, sit=False):
    dicionario_notas = {}

    qtd_notes = 0
    maior = None
    menor = None
    media = 0

    for i in range(0, len(notes)):
        if maior is None or notes[i] > maior:
            maior = notes[i]
        if menor is None or notes[i] < menor:
            menor = notes[i]

        media += notes[i]
        qtd_notes += 1

    dicionario_notas['quantidade_notas'] = qtd_notes
    dicionario_notas['maior_nota'] = maior
    dicionario_notas['menor_nota'] = menor
    dicionario_notas['media'] = media / qtd_notes

    if sit:
        if dicionario_notas['media'] <= 4.9:
            dicionario_notas['situação'] = 'Ruim'
        elif dicionario_notas['media'] <= 6.9:
            dicionario_notas['situação'] = 'Recuperação'
        else:
            dicionario_notas['situação'] = 'Boa'

    return dicionario_notas


a = notas(3, 4, 5, 6, 7, sit=True)
print(a)
