i = 0
for c in range(0,6):
    n = int(input("Digite um numero inteiro: "))
    if n % 2 == 0:
        i += n
print("\033[1;34mA soma total foi de {}".format(i))