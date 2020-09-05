#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(a,b,c):
    print(f"Contagem de {a} ate {b} pulando de {c}")
    for n in range(a,b+c,c):
        print(f"  {n}",end=" ")
    print()


#Principal
print(f"{'-='}"*20)
contador(1,10,1)
print(f"{'-='}"*20)
contador(10, 0, -2)
print(f"{'-='}"*20)
a = int(input("Digite que numero sera o inicio da contagem: "))
b = int(input("Digite que numero sera o final contagem: "))
c = int(input("Digite a razão: "))
contador(a,b,c)
print(f"{'-='}"*20)