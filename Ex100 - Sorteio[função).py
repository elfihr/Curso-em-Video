#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
# e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import sample
lista = []


#Funções
def aleatorio(n):
    lista.append(sample(range(n), 5))
    print(f"{'-='}" * 20)
    print(f"Numeros Sorteados {lista}")
    print(f"{'-='}" * 20)
    p = lista[:]


def somapar(n):
    soma = 0
    print(f"Soma dos numeros pares")
    for v in n:
        if v % 2 == 0:
            soma += v
    print(soma)


#Principal
print(f"{'-='}"*20)
while True:
    while True:
        start = str(input("Inicia o programa?[S/N]: ")).strip()[0].upper()
        if start in "SN":
            break
        print("ERROR")
    if start in "S":
        n = int(input("\nQuantos você quer sortear?[Numero >=5]: "))
        aleatorio(n)
        somapar(lista)
    if start == "N":
        break

print(f"FIM DO PROGRAMA")