a = int(input("\033[1;31mDigite um numero inteiro: "))
b = int(input("\033[1;32mDigite outro numero: "))
c = int(input("\033[1;33mDigite mais um numero: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print("\033[1;34mO menor valor é {}".format(menor))
maior = b
if a > b and a > c:
    maior = a
if c > b and c > a:
    maior = c
print("\033[1;34mO maior o numero é {}".format(maior))