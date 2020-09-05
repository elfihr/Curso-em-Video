#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista.
#No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
menor = maior = 0
principal = []
temp = []
while True:
    temp.append(str(input("NOME: ")))
    temp.append(float(input("PESO: ")))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = " "
    while resp not in "NS":
        resp = str(input("Quer continuar?[S/N]: ")).strip().upper()[0]
    if resp in "N":
        break
print(f"Dados cadastrados: {principal}")
print(f"Foram cadastrados {len(principal)} pessoas")
print(f"O maior peso {maior}Kg de ",end=" ")
for p in principal:
    if p[1] == maior:
        print(f"[{p[0]}]",end=" ")
print(f"\nO menor peso {menor}Kg",end=" ")
for p in principal:
    if p[1] == menor:
        print(f"[{p[0]}]",end=" ")