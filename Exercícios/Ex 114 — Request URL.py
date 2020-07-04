import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print(f'\033[5:31mO site não está acessível.')
else:
    print('\033[5:32mO site está acessível, acessa lá!')
