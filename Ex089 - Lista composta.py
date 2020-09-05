#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde
#tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o
#usuário possa mostrar as notas de cada aluno individualmente.
sistema = []
temp = []
while True:
    name = str(input("NOME: "))
    med1 = float(input("NOTA 1: "))
    med2 = float(input("NOTA 2: "))
    media = (med1+med2) /2
    temp.append([name,[med1,med2],media])
    resp = str(input("Quer continuar?[S/N]: ")).strip().upper()[0]
    if resp in "N":
        break

print(f"{'Nº':<4}{'NOME':<10}{'MEDIA':<20}")
for n, d in enumerate(temp):
    print(f"{n:<4}{d[0]:<10}{d[2]:<20}")

while True:
    number = int(input("Gostaria de ver a nota de qual aluno?(999 para fechar): "))
    if number == 999:
        break
    if number <= len(temp) - 1:
        print(f"O aluno(a) {temp[number][0]} tirou {temp[number][1]}")
print(f"FINALIZANDO PROGRAMA")