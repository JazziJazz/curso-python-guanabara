#  Programa que lê uma frase digitada pelo usuário e exibe na tela o resultado; é palindromo ou não?

frase = input('Digite uma frase, iremos fazer uma verificação para você e exibiremos na tela o resultado se for'
              ' um palindromo.\nResposta: ').strip().upper().replace(' ', '')

if frase[::-1] == frase:
    print(
        f"\033[1:34mA frase digitada por você for {frase}, ela é um palindromo pois o seu reverso fica {frase[::-1]}.")
else:
    print(
        f'\033[1:31mA frase digitada por você for {frase}, ela NÃO é um palindromo pois o seu reverso fica '
        f'{frase[::-1]}.')
