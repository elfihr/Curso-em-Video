soma = cont = 0
while True:
    n = int(input("Digite um numero inteiro[Digite 999 para parar]: "))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"A soma foi {soma} e foram digitados {cont} números")