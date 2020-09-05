list = ("lápis", 1.20, "borracha", 0.8, "caderno", 6.00)


print(f'{"TABELA DE PREÇOS":>30}')
for c in range(0,len(list)):
    if c % 2 == 0:
        print(f"{list[c]:.<30}",end=" ")
    else:
        print(f"{list[c]:>7}")