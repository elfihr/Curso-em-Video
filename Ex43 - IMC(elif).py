p = float(input("Quanto você pesa?: "))
a = float(input("Qual a sua altura?: "))

imc = p / (a * 2)

print("\033[1;34mO IMC é {:.2f}".format(imc))

if imc <= 18.5:
    print("Abaixo do peso")
elif 18.5 < imc <= 25:
    print("Peso ideal")
elif 25 < imc <= 30:
    print("Sobrepeso")
elif 30 < imc <= 40:
    print("Obesidade")
else:
    print("Obesidade morbida")