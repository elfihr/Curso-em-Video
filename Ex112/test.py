#Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja
# capaz de funcionar como a função imputa(), mas com uma validação de dados para
# aceitar apenas valores que seja monetários.

from Ex112.ultilidades import moeda, dado
n = dado.leiaDinheiro("Digite um valor: ")
p = int(input("Porcentagem a modifivar: "))

moeda.resumo(n,p)

