print("Vamos descoobrir se é possivel fazer o triangulo e qual tipo ele é")

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite mais um numero: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("É possivel montar o triangulo")
    if n1 == n2 == n3:
        print("É um triangulo equilatero")
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print("É um triangulo isoceles, ou seja dois lados iguais")
    else:
        print("O trinagulo é escaleno e possue lados diferentes")
else:
    print("Não pe possivel mosntar um triangulo")