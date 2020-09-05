idade = 0
cont = 0
tot = 0
maioridadehomem = 0
mulhermenosde20 = 0
nomevelho = " "
for p in range(1, 5):
    print("----------{}ºPESSOA----------".format(p))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[F/M]: ".strip()))
    cont = cont + idade
    cont = idade + cont
    if p == 1 and sexo in "Mm":
        maioridadehomem += idade
        nomevelho = nome
    if sexo in "Mn" and maioridadehomem < idade:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        mulhermenosde20 += 1


tot = cont/4
print("A média de idade foi de {} anos".format(tot))
print("O homem mais velho do grupo é {}".format(nomevelho))
print("O grupo tem {} pessoas do sexo feminino com menos de 20 anos".format(mulhermenosde20))

