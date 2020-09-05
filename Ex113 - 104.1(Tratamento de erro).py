#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except Exception as Erro:
            print(f"{Erro.__class__}")
            continue
        except (KeyboardInterrupt):
            return 0

        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except Exception as error:
            print(error.__class__)
        else:
            return n




z = leiaFloat("Digite um numero: ")
print('-'*10)
print(z)

