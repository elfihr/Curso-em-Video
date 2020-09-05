c = int(input("\033[1;31mDigite um número inteiro: "))
if c % 2 == 0:
    print("\033[1;34mO número {} é par".format(c))
else:
    print("\033[4;34mO número {} é impar".format(c))