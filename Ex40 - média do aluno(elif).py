print("-=" * 20)
print("\033[1;32mVAMOS CALCULAR A MÉDIA DO ALUNO\033[m")
print("-+" * 20)

n1 = float(input("\033[1;32mDigite a primeira nota: "))
n2 = float(input("\033[1;36mDigite a segunda nota: "))

m = (n1 + n2) / 2

print("\033[1;35mA sua nota final foi de {}\033[m".format(m))

if m >= 6:
    print("\033[1;34mParabêns você foi APROVADO")
elif m >= 4 and m < 6:
    print("\033[1;34m Você não tirou nota suficiente para aprovação, tera que fazer RECUPERAÇÂO")
else:
    print("\033[1;34mVocê foi REPROVADO")