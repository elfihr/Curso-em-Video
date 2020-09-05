#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie
#duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.

a = list()
b = list()
c = list()
resp = " "
while True:
    c.append(int(input("Digite um numero: ")))
    resp = str(input("Quer continuar[S/N]: ")).strip().upper()[0]
    if resp in "N":
        break
for n, val in enumerate(c):
    if val % 2 == 0:
        a.append(a)
    elif val % 2 == 1:
        b.append(b)

print(f"Todos os valores digitados são {sorted(c)}")
print(f"Os valores impares foram {b}")
print(f"Os valores pares foram {a}")
