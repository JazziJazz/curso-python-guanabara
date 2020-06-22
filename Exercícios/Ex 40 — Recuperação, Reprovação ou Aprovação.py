#  Programa que lê duas notas de um aluno, exibe sua média e se for abaixo de cinco então ele está reprovado, se for
#  entre cinco e seis virgula nove, ele está de recuperação, se for acima de sete ele está aprovado.

nota_um = float(input('Digite a primeira nota do aluno: '))
nota_two = float(input('Digite a segunda nota do aluno: '))
media = (nota_um + nota_two) / 2

if media < 5:
    print(f'É trágico mas a nota do aluno foi muito baixa, portanto ele está reprovado, sua nota foi de: {media:.2f}.')
elif 5 < media < 6.9:
    print(f'Ainda há esperança. O aluno ficou de recuperação, sua nota foi de: {media:.2f}.')

if media > 6.9:
    print(f'O aluno está aprovado! Parabéns, a nota do aluno foi de: {media:.2f}.')
