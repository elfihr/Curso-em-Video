F = ""
M = ""
s = str(input("Digite seu sexo: ")).strip().upper()[0]
while s not in "MF":
    s = str(input("Sexo invalido, digite novamente: ")).upper()[0].split()
    if s == F:
        s = "feminino"
    else:
        s = "masculino"
print("O sexo seleciona é: {}".format(s))