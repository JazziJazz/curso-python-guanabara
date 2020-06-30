#  Programa que salva o nome, a média e exibe as informações e a situação do aluno. Usanod dicionário, é claro.

alunos = {'nome': input('Qual o nome do aluno?: ').title().strip(),
          'media': float(input('Qual a média do aluno?: '))}

if alunos['media'] >= 7:
    alunos['situação'] = 'Aprovado'
else:
    alunos['situação'] = 'Reprovado'

print(f'O aluno {alunos["nome"]} obteve a média igual a: {alunos["media"]}. A sua situação atual é: '
      f'{alunos["situação"]}.')
