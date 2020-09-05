print("\033[1;35mDê as medidas das retas do triangulo")
r1 = float(input("\033[1;31mDigite o primeiro comprimento: "))
r2 = float(input("\033[1;31mDigite o segundo comprimento: "))
r3 = float(input("\033[1;31mDigite o terceiro valor: "))

if r2 < r1 + r3 and r1 < r2 + r3 and r3 < r1 + r2:
    print("\033[1;34mÈ possivel fazer o triangulo")
else:
    print("\033[1;34mInfelizmente não da. È nescessario q a soma das menores medidas de maior que a maior medida")

