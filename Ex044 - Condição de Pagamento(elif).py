p = float(input("\033[1;33mQual o preço do produto?: "))
c = str(input("\033[1;32mQual a forma de pagamento?: \033[m \033[1;34m\n>dinheiro ou cheque \n>cartao a vista \n>2x no cartao \n>3x no cartao \033[m \nDigite a forma de pagamento: "))

print("O produto custa {}".format(p))

if c == "dinheiro" or c == "cheque":
    v = p - p * 0.1
    print("Pagando a vista o preço cai para {} reais".format(v))
elif c == "cartao a vista":
    v = p - p * 0.05
    print("Pagando a vista no cartao o preço final é {} reais".format(v))
elif c == "2x no cartao":
    print("Serão duas parcelas de {} reais".format(v))
elif c == "3x no cartao":
    v = p + p * 0.2
    print("Serão 3 parcelas de {} reais".format(v / 3))
