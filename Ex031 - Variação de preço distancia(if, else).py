d = float(input("\033[1;31mQual a distância da viagem?: "))
if d <= 200:
    p = d * 0.5
    print("\033[4;34m O preço da viagem é {:.2f} reais".format(p))
else:
    p = d * 0.4
    print("\033[4;34m O preço da passagem é {:.2f} reais".format(p))