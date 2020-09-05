v = float(input("\033[1;31mQual a velocidade do carro: "))
if v <= 80.0:
    print("\033[4;34mVocê é um bom motorista")
else:
    m = (v - 80) * 7
    print("\033[4;34mVocê foi multado em {} reais".format(m))