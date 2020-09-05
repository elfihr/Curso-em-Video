n = int(input("Digite um numero inteiro: "))
cont = 0
for d in range(1, n+1):
    if n % d == 0:
        print("\033[1;31m{}\033[m".format(d), end=" ")
        cont = cont + 1
    else:
        print("\033[1;36m{}\033[m".format(d), end=" ")
if cont == 2:
    print("\nO numero {} é primo".format(n))
else:
    print("\nO numero {} foi divisivel {}, logo não é primo".format(n, cont))