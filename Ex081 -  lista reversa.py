#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

note = []
while True:
    note.append(int(input("digite um valor")))
    resp = str(input("Quer continuar[S/N]: ")).upper().strip()[0]
    if resp in "N":
        break
note.sort( reverse=True)
print(f"Foram digitados {len(note)}")
if 5 in note:
    print(f"O valor 5 esta na posição {note.index(5)}...")
else:
    print("O valor 5 não foi digitado...")
print(f"\033[1;34m{note}")
