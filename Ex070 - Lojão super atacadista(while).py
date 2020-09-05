tot = cheapprice = price = expenciveprice = 0
cheap = " "
print("{:-^40}".format("SALDÃO DO FAUSTÃO"))
while True:
    name = str(input("Digite o nome do produto:R$"))
    price = float(input("Digite o preço: "))
    tot += price
    if price > cheapprice:
        cheapprice = price
        cheap = name
    if price > expenciveprice:
        expenciveprice = price
    choice = " "
    while choice not in "SN":
        choice = str(input("Quer comprar um novo produto?:")).upper().strip()[0]
    if choice == "N":
        break
print("{:-^40}".format("FIM DO PROGRAMA"))
print(f"A compra mais cara foi de R${expenciveprice:.2f}")
print(f"A compra deu um total de R${tot:.2f}")
print(f"A compra mais barata foi {cheap} de R${cheapprice:.2f}")
