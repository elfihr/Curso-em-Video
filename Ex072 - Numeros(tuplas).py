
grupo = ("zero", "um", "dois", "três","quatro", "cinco", "Seis", "sete", "oito", "nove", "dez")
while True:
    n = int(input("Digite um numero[00 a 10]: "))
    if n in range(0, 10):
        print(f"Você escolheu o numero {grupo[n]}")

    resp = str(input("Você quer continuar[S/N]: ").upper().strip()[0])
    if resp in "N":
        break

print("FIM DO PROGRAMA")