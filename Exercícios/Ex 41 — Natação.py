#  Programa que lê a data de nascimento de um aluno e exibe em qual categoria de natação este futuro atleta pode ser
#  encaixado. Até nove anos, mirim. Até quatorze anos, infantil. Até dezenove anos, júnior. Até vinte anos, sênior.
from datetime import datetime

ano = datetime.today().year
ano_nascimento = int(input('Em que ano o aluno nasceu?\nResposta: '))
idade = (ano - ano_nascimento)

if idade <= 9:
    print(f'O atleta tem {idade} anos. Portanto, ele será colocado na categoria mirim.')
elif 9 < idade <= 14:
    print(f'O atleta tem {idade} anos. Portanto, ele será colocado na categoria infantil.')
elif 14 < idade <= 19:
    print(f'O atleta tem {idade} anos. Portanto, ele será colocado na categoria júnior.')
elif 20 <= idade < 21:
    print(f'O atleta tem {idade} anos. Portanto, ele será colocado na categoria sênior.')
else:
    print(f'O atleta tem {idade} anos. Portanto, ele será colocado na categoria master.')
