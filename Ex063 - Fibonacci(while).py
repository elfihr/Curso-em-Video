print("   GERADOR DE FIBONACCI")
print(10 * "=-")
past = future = cont = 0
present = 1
choice = int(input("Quantos termos da sequencia de Fibonacci você quer ver?: "))

while True:
    print(f"{future} -> ",end=" ")
    if cont == choice:
        break
    past = present
    present = future
    future = past + present
    cont += 1

print("FIM")