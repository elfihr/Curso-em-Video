n = r = 0
while True:
    n = int(input("Quer ver a tabuada de qual numero: "))
    if n <= 0:
        break
    for c in range(1, 11):
       r = n * c
       print(f"{n} X {c} = {r}")
print("Obrigado por testar nosso programa")