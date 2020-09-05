#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

#LOCAL
def leiaint(msg):
    ok=False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok =True
        else:
            print("ERROR!Digite um numero valido")
        if ok:
            break
    return valor


#GLOBAL
n = leiaint("Digite um numero: ")
print('-'*20)
print(f"Número Digitado {n}")
print('-'*20)