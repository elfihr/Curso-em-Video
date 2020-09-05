#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from Ex107 import moedas
n = float(input("Digite um preço: "))
p = int(input("Porcentagem a modifivar: "))
m1 = moedas.aumentar(n,p)
m2 = moedas.diminuir(n,p)
m3 = moedas.dobro(n)
m4 = moedas.metade(n)
print(f"{p}% a mais de {n} é {m1}\n{p}% a menos de {n} é {m2}\nO dobro de {n} é {m3}\nA metade de {n} é {m4}")

