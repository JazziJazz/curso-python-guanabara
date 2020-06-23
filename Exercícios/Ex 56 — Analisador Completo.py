#  Programa que lê o nome, idade e sexo de um grupo de pessoas, exibe na tela o nome e idade do homem mais velho, a
#  quantidade de pessoas do sexo masculino, a quantidade de pessoas do sexo feminino, a média de idade do grupo, e
#  quantas mulheres tem menos de vinte anos.
from time import sleep

tamanho_grupo = int(input('Digite a quantidade de pessoas presentes no grupo que deseja analisar.\nResposta: '))
mulheres_menores = 0
media_idade = 0
quantidade_feminino = 0
quantidade_masculino = 0
homem_mais_velho = None
idade_mais_velho = 0

for i in range(1, tamanho_grupo + 1):
    print(f'\033[1:34m—————— {i}ª Pessoa ——————')

    nome = input('\033[1:32mQual o nome?: ').strip().title()
    idade = int(input('\033[1:32mQual a idade?: '))
    sexo = input('\033[1:32mSexo [M/F]: ').strip().upper()

    sleep(1.5)

    if sexo == 'M':
        if homem_mais_velho is None or (idade > idade_mais_velho):
            idade_mais_velho = idade
            homem_mais_velho = nome
        quantidade_masculino += 1
        media_idade += idade
    else:
        if idade < 20:
            mulheres_menores += 1
        quantidade_feminino += 1
        media_idade += idade

print(f'\033[1:35mO nome do homem mais velho é: {homem_mais_velho}, ele está na casa dos {idade_mais_velho} anos.\n'
      f'Ao total houve uma quantidade de {quantidade_masculino} participantes do sexo masculino e {quantidade_feminino}'
      f' do sexo feminino.\nA média de idade de todos os participantes é de: {media_idade / tamanho_grupo}.'
      f'\nHouve um total de {mulheres_menores} mulheres menores de vinte anos.')