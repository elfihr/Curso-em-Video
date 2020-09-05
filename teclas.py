# /  barra
# \  invertida

try:
    a = int(input("number: "))
    b = int(input("number: "))
    c = a+b
except Exception as erro:
    print(f"O erro foi {erro.__class__}")
else:
    print(c)
finally:
    print("Fechando Programa")





