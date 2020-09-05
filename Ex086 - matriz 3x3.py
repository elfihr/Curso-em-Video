#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com
#valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

listao = [[],[],[]]
for c in range(0,3):
    listao[0].append(int(input(f"Digite o valor para [0-{c}]: ")))
for d in range(0,3):
    listao[1].append(int(input(f"Digite o valor para [1-{d}]: ")))
for e in range(0,3):
    listao[2].append(int(input(f"Digite o valor para [2-{e}]: ")))

print(f"{listao[0]:^5}")
print(f"{listao[1]:^5}")
print(f"{listao[2]:^5}")

#usar for c in range(  ):
#         for d in range( ):
#listao[c][d] = int(inpu.....
#para linhas e colunas