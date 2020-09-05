soma = 0
cont = 0
for c in range(0, 501, 2):
    if c % 3 == 0:
        soma = c + soma
        cont = cont + 1
print("\033[1;34mOs {} valores impares divisiveis por 3 é {} ".format(cont, soma))
