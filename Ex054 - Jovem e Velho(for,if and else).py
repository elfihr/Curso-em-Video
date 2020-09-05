from datetime import date
atual = date.today().year
cont = 0
contn = 0
for c in range(1, 8):
    nasc = int(input("Em que ano a {}º pessoa nasceu? ".format(c)))
    idade = atual - nasc
    if idade >= 18:
         cont += 1
    else:
        contn += 1
print("{} pessoas tem idade igual ou maior de 18 anos e {} são menores de idade".format(cont, contn))