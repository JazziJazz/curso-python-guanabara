# Programa que lê o nome completo de uma pessoa e analisa o texto, retornando diversas informações.

name = input('Digite o seu nome completo: ')
numero = len(name.replace(' ', ''))
first_name = name.split(' ')[0]

print(f'O seu nome completo em letras maiúsculas: {name.upper()}.\n'
      f'O seu nome completo em letras minúsculas: {name.lower()}.\n'
      f'O seu nome completo tem um total de: {numero} letras.\n'
      f'O seu primeiro nome é igual a: {first_name}.')
