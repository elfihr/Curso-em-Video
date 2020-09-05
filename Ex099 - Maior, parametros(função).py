#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
cont = n = maior = nm = 0
sistema = []


def calc(* núm):
    maior = cont = 0
    for v in núm:
        print(v,end=" ")
        if v > maior:
            maior = v
            cont += 1
    print(f"\nForam analisados {cont} numeros")
    print(f"O maior valor foi {maior}")
    print(f"{'-='}"*20)


calc(1,4,6,9)
calc(4,6,20,5)
calc(1)





