#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com
#valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

listao = [[0,0,0],[0,0,0],[0,0,0]]
soma = somaC3 = maiorL2 = 0
for l in range(0,3):
    for c in range(0,3):
        listao[l][c] = int(input(f"Digite o valor para ({l},{c}): "))
        if listao[l][c] % 2 == 0:
            soma = soma + listao[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f"[{listao[l][c]:^5}]", end=" ")
    print()
print(f"A soma dos numeros pares foi {soma}")

for l in range(0,3):
    somaC3 += listao[l][2]
print(f"Valores da terceira coluna {somaC3}")

for c in range(0,3):
    if c == 0:
        maiorL2 = listao[1][c]
    elif maiorL2 < listao[1][c]:
         maiorL2 = listao[1][c]
print(f"{maiorL2}")
