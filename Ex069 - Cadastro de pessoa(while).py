contman = contwoman = contage = 0
print("=-"*20)
print("{:-^20}".format("PROGRAMA DE CADASTRO"))
print("=-"*20)
print("Cadastre uma pessoa: ")
while True:
    print("Digite a idade: ")
    age = int(input("IDADE: "))
    sex = " "
    while sex not in "HM":
        print("Digite o sexo da pessoa[H/M]: ")
        sex = str(input("SEXO: ")).upper().strip()[0]
    if sex in "H":
        contman += 1
        if age > 18:
            contage += 1
    elif sex in "M":
        if age < 20:
            contwoman += 1
            if age > 18:
                contage += 1
    choice = " "
    while choice not in "NS":
        choice = str(input("Quer cadastrar mais uma pessoa: ")).upper().strip()[0]
    if choice == "N":
        break
print("=-"*20)
print(f"Foram {contage} pessoas com mais de 18 anos, {contman} homens cadastrados e {contwoman} mulheres com menos de 20 anos")