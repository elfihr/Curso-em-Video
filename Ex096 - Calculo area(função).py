#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
# terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l,c):
    print(f'A area total é {l*c}m²')


#Sistema
l = float(input("Digite a largura: "))
c = float(input("Digite o comprimento: "))
area(l,c)