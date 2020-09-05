#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
#cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
soma = 0
cadas = {}
sistema = []
while True:
    cadas['Nome'] = str(input("NOME: "))
    cadas['Sexo'] = " "
    while True:
        cadas['Sexo'] = str(input("SEXO[M/F]:")).strip().upper()[0]
        if cadas['Sexo'] in "MF":
            break
    cadas['Idade'] = int(input("IDADE: "))
    soma += cadas['Idade']
    sistema.append(cadas)

    while True:
        resp = str(input("Quer continuar[S/N]: ")).strip().upper()[0]
        if resp in "NS":
            break
        print("ERROR 404")
    if resp in "N":
        break
print("-="*50)
print(f"{'ISTA DE DADOS'}:-^50")
print("-="*50)  
print(f"->PESSOAS CADASTRADAS: {sistema.count(cadas)}")
#{len(sistema)}
media = soma / len(sistema)
print(f"->MÉDIA DE IDADE: {media:.2f} anos")
print("->MULHERES CADASTRADAS: ",end="")
for c in sistema:
    if c['Sexo'] in "F":
        print(f'{c["Nome"]}',end =" ")
    print()
print(f"->PESSOAS COM IDADE ACIMA DE MÉDIA: ",end=" ")
for i in sistema:
    if i['Idade'] > media:
        print(f"{i['Nome']}", end=" ")