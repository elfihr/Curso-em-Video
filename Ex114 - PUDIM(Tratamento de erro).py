#Exercício Python 114: Crie um código em Python que teste se o site pudim está
# acessível pelo computador usado.

import urllib
import urllib.request

try:
    urllib.request.urlopen('https://g1.globo.com/')
except:
    print("Indisponivel no momento")
else:
    print('Tudo Ok')