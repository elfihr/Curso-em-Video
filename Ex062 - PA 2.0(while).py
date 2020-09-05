print("   GERADOR DE PA")
print(10 * "=-")
tn = 1
countn = 0

t = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razao: "))
count = 0

while count < 10:
    print("{} -> ".format(t),end=" ")
    t += r
    count += 1
    countn += 1

while tn != 0:
    tn = int(input("\nQuantos termos você quer a mais?: "))
    count = 0
    while count < tn:
        t += r
        print("{} -> ".format(t), end=" ")
        count += 1
        countn += 1

print("\nForam {} termos\nObrigado por usar o nosso programa".format(countn))

