from Modulos import Real
print("{:^30}".format("BANCO DA QUEBRADEIRA"))
div = cel50 = cel20 = cel10 = cel1 = 0
saque = int(input("Quanto você quer sacar?:R$ "))
recebe = saque
while True:
    if recebe >= 50:
        recebe -= 50
        cel50 += 1
    else:
        if recebe >= 20:
            recebe -= 20
            cel20 += 1
        elif recebe >= 10:
            recebe -= 10
            cel10 += 1
        elif recebe >= 1:
            recebe -= 1
            cel1 += 1
        if recebe == 0:
            break
print(f"{Real.moeda(cel50)} de 50")
print(f"{cel20} de 50")
print(f"{cel10} de 50")
print(f"{cel1} de 50")
print(":-^20".format("FIM DA OPERAÇÃO"))