#  Programa que lê vários números, soma todos eles e informa quantos números foram adicionados. Quando a flag do número
#  999 é digitada, ele para e imprime na tela os resultados.

funcionando = True
cont = 0
soma = 0

while funcionando is True:
    number = float(input('\033[5:34mDigite um número para somar. Para parar digite [999].\n\033[5:30mNúmero: '))
    if not number == 999:
        soma += number
        cont += 1
    else:
        print(f'\033[5:32mAo total você digitou {cont} números. A soma entre eles é de: {soma:.2f}.')
        funcionando = False
