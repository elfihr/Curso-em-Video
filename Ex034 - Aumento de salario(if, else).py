from Modulos import Real
s = float(input("\033[1;33mQual o sálario do funcionario: "))

if s >= 2250.00:
    sa = s * 0.1
    sf = sa + s
    print(f"\033[1;34m O salario agora é {Real.moeda(sf)} e teve um aumento de {Real.moeda(sa)}")
else:
    sa = s * 0.15
    sf = sa + s
    print(f"\033[1;34mO salario aumentou para {Real.moeda(sf)} e teve um aumento de {Real.moeda(sa)}")