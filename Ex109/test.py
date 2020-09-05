#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um
# parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

from Ex109 import moedas
n = float(input("Digite um preço: "))
p = int(input("Porcentagem a modifivar: "))
print('-'*40)
print(f"Adicionando {p}% a mais de {moedas.monetario(n)} é {moedas.aumentar(n,p,True)}"
      f"\nAdicionando {p}% a menos de {moedas.monetario(n)} é {moedas.diminuir(n,p,True)}"
      f"\nO dobro de {moedas.monetario(n)} é {moedas.dobro(n,True)}"
      f"\nA metade de {moedas.monetario(n)} é {moedas.metade(n,True)}")
print('-'*40)
help(moedas.aumentar())