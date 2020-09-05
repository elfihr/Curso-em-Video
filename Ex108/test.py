#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from Ex108 import moedas
n = float(input("Digite um preço: "))
p = int(input("Porcentagem a modifivar: "))

print(f"Adicionando {p}% a mais de {moedas.monetario(n)} é {moedas.monetario(moedas.aumentar(n,p))}"
      f"\nAdicionando {p}% a menos de {moedas.monetario(n)} é {moedas.monetario(moedas.diminuir(n,p))}"
      f"\nO dobro de {moedas.monetario(n)} é {moedas.monetario(moedas.dobro(n))}"
      f"\nA metade de {moedas.monetario(n)} é {moedas.monetario(moedas.metade(n))}")