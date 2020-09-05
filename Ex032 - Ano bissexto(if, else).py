a = int(input("\033[1;31mDigite um ano: "))

if a % 4 == 0:
    print("\033[1;34mEste é um ano bissexto!")
else:
    print("\033[1;34mEste não é um ano bissexto")