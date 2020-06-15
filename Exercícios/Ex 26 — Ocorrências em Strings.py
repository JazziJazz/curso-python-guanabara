#  Programa que analisa profundamente uma string, verificando a quantidade de vezes que uma determinada letra
#  Aparece em uma string, além da primeira e última vez que essa mesma letra aparece.

"""
name = input('Qual é o seu nome?\nRESPOSTA: ')
letra = input('Qual letra você deseja obter informações?\nRESPOSTA: ')

if letra in name: #  Código feito sem métodos, eu não me recordava em época da existência destes.
    quantidade = 0
    primeiro = None
    ultimo = None

    for i in range(len(name)):
        if letra == name[i]:
            quantidade += 1

            if primeiro is None:
                primeiro = i

    for i in range(len(name), -1, -1):
        if ultimo is None:
            ultimo = i

    print(f'A letra {letra} aparece nessa string uma quantidade de {quantidade} vezes.\nA primeira vez que aparece'
          f' é na posição {primeiro} e a última na posição {ultimo}.')"""

name = input('Qual é o seu nome?\nRESPOSTA: ').strip().upper()
letra = input('Qual letra você deseja obter informações?\nRESPOSTA: ').upper()

print(f"A letra {letra} aparece uma quantidade de {name.count(letra)} vezes.\n"
      f"A primeira letra selecionada aparece na posição {name.find(letra)}.\n"
      f"A última vez aparece em {name.rfind(letra)}.")
