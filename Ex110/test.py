#Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada
# resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo
# criado até aqui.

from Ex110 import moedas
n = float(input("Digite um preço: "))
p = int(input("Porcentagem a modifivar: "))

moedas.resumo(n,p)

