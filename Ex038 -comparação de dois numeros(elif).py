n1 = int(input("\033[1;31mDigite um nuemro inteiro: "))
n2 = int(input("\033[1;31mDigite outro numero inteiro: "))

if n1 > n2:
    print("\033[1;34mO valor {} é maior que {}".format(n1, n2))
elif n2 > n1:
    print("\033[1;34mO numero {} é maior que {}".format(n2, n1))
else:
    print("\033[1;34m{} e {} são iguais".format(n1, n2))