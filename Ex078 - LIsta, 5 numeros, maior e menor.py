#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
#qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


n = list(int(input(f"Digite um numero na posição {f}: "))for f in range(0,5))

maior = max(n)
menor = min(n)

print(f"O maior valor foi {max(n)}\nE aparece nas posições:")
for val, pit in enumerate(n):
    if pit == maior:
        print(f"{val} posição ->", end=" ")
print(f"O menor valor foi {min(n)}\nE aparece nas posições:")
for val, pit in enumerate(n):
    if pit == menor:
        print(f"{val} posição ->", end=" ")



