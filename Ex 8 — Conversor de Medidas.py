# Programa que converte uma medida em centimetros para metros, ou de metors para milimetros.

def conversor():
    resposta = int(input('Digite o número referente a sua opção:\n\n(1). Metro(s).\n(2). Centímetros(s).\n(3). Milímetro(s).\n\nResposta: '))

    while (resposta > 3) or (resposta < 1):
        print('Resposta inválida. Só há três opções, verifique o que você digitou e responda novamente.')
        resposta = int(input('Digite o número referente a sua opção:\n\n(1). Metro(s).\n(2). Centímetros(s).\n(3). Milímetro(s).\n\nResposta: '))

    if (resposta == 1):
        calculo = int(input('Digite a medida em metros: '))
        print(f'Em {calculo} metro(s). há {calculo * 100} centimetro(s).\nE há {calculo * 1000} milímetro(s).')


    if (resposta == 2):
        calculo = int(input('Digite a medida em centimetros: '))
        print(f'Em {calculo} centimetro(s) há {calculo / 100} metro(s).\nE há {calculo * 10} milímetro(s).')

    if (resposta == 3):
        calculo = int(input('Digite a medida em milimetros: '))
        print(f'Em {calculo} milimetros(s) há {calculo / 10} centimetro(s).\nE há {calculo / 100} metros(s).')

conversor()
program = input('Deseja finalizar o programa?\nResposta(S/N): ').upper()

while (program == 'N') or (program != 'S'):
    program = input('Deseja finalizar o programa?\nResposta(S/N): ').upper()
    conversor()

print('Foi um prazer. Fim do programa.')
