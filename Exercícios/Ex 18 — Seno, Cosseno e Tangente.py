# Programa que lê o valor de um ângulo e encontra seu seno, cosseno e também a tangente, eibindo-os na tela.
from math import sin, cos, tan, radians

ang = int(input('Qual o valor do ângulo?: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tang = tan(radians(ang))

print(f'O seno é equivalente a {seno:.2f}.\nO cosseno é equivalente a {cosseno:.2f}.\nPor fim, a tangente equivale a {tang:.2f}.')
