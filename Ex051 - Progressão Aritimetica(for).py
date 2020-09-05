print('=' * 50)
print('                \033[1;34MRAZÃO  ARITMÉTICA ')
print('=' * 50)
r = int(input("Qual é a razão: "))
n = int(input("Por qual numero começara a razão: "))

for c in range(0,10):
    print(n, end=' -> ')
    n += r
