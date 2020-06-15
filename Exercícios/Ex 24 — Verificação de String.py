# Programa que lê a cidade em que um usuário nasceu e retorna True se começar com a palavra 'Santo'.

"""cidade = input('Qual seu local de origem?\nRESPOSTA: ').upper().replace(' ', '')

if 'SANTO' in cidade:
    print('True')
else:
    print('False')"""

cidade = input('Qual é o seu local de origem?\nRESPOSTA: ').strip().lower()

if (cidade[:5] == 'santo'):
    print('Sua cidade começa com Santo, que legal!')
else:
    print('Sua cidade não começa com Santo, deslike.')
