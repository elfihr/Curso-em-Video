#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
#lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
note = list()
n = 0
note = []
while True:
    print("Adicionando um valor...")
    n = int(input("Digite: "))
    if n not in note:
        note.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado")
    resp = str(input("Qweu continuar{S/N]:")).strip().upper()[0]
    if resp in "N":
        break
print(f"{sorted(note)}")


