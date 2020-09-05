#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
#cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.

principal = [[],[]]
for cont in range(0,7):
    n = int(input(f"Digite {cont +1}º valor: "))
    if n % 2 == 0:
        principal[0].append(n)
    else:
        principal[1].append(n)
print("-=" * 30)
print(f"Todos os numeros digitados: {principal}")
print(f"Numeros pares {sorted(principal[0])}")
print(f"Numeros impares {sorted(principal[1])}")

