n = int(input("Digite um numero para realizar a operação fatorial: "))
c = n
t = 1
print("Calculando fatorial de {}! =".format(n), end=" ")

while c > 0:
    print("{}".format(n), end=" ")
    print(" X " if c > 0 else " = ",end=" " )
    c -= 1
    t *= n
    n = n-1

print("= {}".format(t), end=" ")
