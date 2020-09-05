t = int(input('Digite o primeiro termo: '))
r = int(input("Digite a razão"))
count = 0

while count < 10:
    print("{} -> ".format(t),end=" ")
    t = t + r
    count += 1

print("kabo")