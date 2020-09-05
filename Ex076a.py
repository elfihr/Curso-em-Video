itens = ("lápis", 1.20, "borracha", 0.8, "caderno", 6.00)

print(f'{"LISTA DE MATERIAIS:=^30"}')
for p in range(0, len(itens), 2):
    print('{:.<20}  {:>6.2f}'.format(itens[p], itens[p + 1]))
