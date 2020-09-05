#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
cont = 0

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um segundo numero: "))
n3 = int(input("Digite um terceiro numero: "))
n4 = int(input("Digite um quarto numero: "))

list = (n1, n2, n3, n4)

print(f"Numeros sorteados: {list}")
print(f"O numero 9 apareceu {list.count(9)} vezes")
if 3 in list:
    print(f"O numero 3 apareceu na posição {list.index(3) + 1}ª posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
    print("Os numeros pares digitados foram: ", end=" ")
for n in list:
    if n % 2 == 0:
            print(n, end=" ")