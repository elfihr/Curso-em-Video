i = int(input("Digite ano de nascimento do atleta: "))
a = int(input("Em que ano estamos: "))

c = a - i

print("\033[1;35mO atleta tem {} anos".format(c))

if c <= 9:
    print("Esta na categoria Mirim")
elif c <= 14 and c > 9:
    print("Esta na categoria Infantil")
elif c <= 19 and c > 14:
    print("Esta na categoria Junior")
elif c == 20:
    print("Esta na categoria Senior")
else:
    print("Esta na categoria Master")