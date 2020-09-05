#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
#lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

note = []
for c in range(0,5):
    n = int(input("Digite um numero: "))
#
    if c == 0 or n > note[-1]:
        note.append(n)
        print("Valor adicionado na ultima posição...")
    else:
        pos = 0
        while pos < len(note):
            if n <= note[pos]:
                note.insert(pos,n)
                print(f"Adicionado na posição {pos}")
                break
            pos += 1
print(note)

